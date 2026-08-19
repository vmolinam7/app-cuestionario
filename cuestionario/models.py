from django.db import models

class Pregunta(models.Model):
    OPCIONES_CHOICES = [
        ('A', 'Opción A'),
        ('B', 'Opción B'),
        ('C', 'Opción C'),
        ('D', 'Opción D'),
    ]

    categoria = models.CharField(max_length=250, default='General', verbose_name="Categoría / Módulo")
    texto = models.TextField(verbose_name="Pregunta")
    opcion_a = models.TextField(verbose_name="Opción A")
    opcion_b = models.TextField(verbose_name="Opción B")
    opcion_c = models.TextField(verbose_name="Opción C")
    opcion_d = models.TextField(verbose_name="Opción D")
    opcion_correcta = models.CharField(max_length=1, choices=OPCIONES_CHOICES, verbose_name="Opción Correcta")
    activa = models.BooleanField(default=True, verbose_name="Activa")
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")

    class Meta:
        verbose_name = "Pregunta"
        verbose_name_plural = "Preguntas"
        ordering = ['id']

    def __str__(self):
        return f"[{self.categoria}] {self.texto[:60]}"


class Participante(models.Model):
    nombres = models.CharField(max_length=150, verbose_name="Nombres")
    apellidos = models.CharField(max_length=150, verbose_name="Apellidos")
    cedula = models.CharField(max_length=30, db_index=True, verbose_name="Número de Cédula / ID")
    fecha_registro = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Registro")

    class Meta:
        verbose_name = "Participante"
        verbose_name_plural = "Participantes"
        ordering = ['-fecha_registro']

    def nombre_completo(self):
        return f"{self.nombres} {self.apellidos}"

    def __str__(self):
        return f"{self.nombre_completo()} - C.I: {self.cedula}"


class IntentoCuestionario(models.Model):
    participante = models.ForeignKey(Participante, on_delete=models.CASCADE, related_name='intentos', verbose_name="Participante")
    puntaje = models.IntegerField(verbose_name="Puntaje Obtenido")
    total_preguntas = models.IntegerField(default=7, verbose_name="Total Preguntas")
    porcentaje = models.FloatField(verbose_name="Porcentaje (%)")
    aprobado = models.BooleanField(default=False, verbose_name="Aprobado")
    respuestas_detalle = models.JSONField(default=dict, verbose_name="Detalle de Respuestas")
    fecha_completado = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Finalización")

    class Meta:
        verbose_name = "Intento de Cuestionario"
        verbose_name_plural = "Intentos de Cuestionarios"
        ordering = ['-fecha_completado']

    def __str__(self):
        estado = "APROBADO" if self.aprobado else "REPROBADO"
        return f"{self.participante.nombre_completo()} - {self.puntaje}/{self.total_preguntas} ({estado})"
