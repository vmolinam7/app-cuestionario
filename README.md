# 🚛 App de Cuestionarios y Evaluación de Conocimiento para Conductores FP

Sistema web desarrollado en **Django 5** con soporte para evaluación dinámica de conductores, panel de administración con métricas, importación y exportación de reportes Excel (`.xlsx`), conexión a base de datos PostgreSQL en **Neon Tech** y configuración lista para despliegue en **Vercel**.

---

## 🌟 Características Principales

- **Vista Pública de Evaluación**:
  - Registro inicial de datos obligatorios: **Nombres**, **Apellidos** y **Cédula / Identificación**.
  - **Selección Aleatoria**: Genera automáticamente **7 preguntas al azar** del banco de preguntas por cada evaluado.
  - **Navegación Paso a Paso**: Interfaz guiada pregunta por pregunta con barra de progreso interactiva.
  - **Restricción de Intento Único por Cédula**: Evita que un mismo conductor vuelva a realizar el test.
  - **Vista de Resultado Segura**: Muestra la calificación final (Aprobado/Reprobado) ocultando el desglose de respuestas para evitar filtraciones de respuestas entre conductores.

- **Panel de Administración Personalizado (`/panel-admin/`)**:
  - **Dashboard de Métricas**: Indicadores de Total de Evaluaciones, Participantes Únicos, Tasa de Aprobación y Promedio General.
  - **Buscador**: Filtro rápido por Cédula o Nombre.
  - **Detalle de Evaluación**: Consulta pregunta por pregunta de lo que respondió cada conductor.
  - **Exportación a Excel Completa (`.xlsx`)**:
    - *Pestaña 1 (Resumen)*: Metadatos generales y calificación.
    - *Pestaña 2 (Detalle Respuestas)*: Pregunta por pregunta con formato condicional en aciertos y desaciertos.
  - **Importación desde Excel**: Cargar o actualizar el banco de preguntas mediante archivo Excel (incluye descarga de plantilla de ejemplo).
  - **Banco de Preguntas**: Crear y activar/desactivar preguntas.

- **Base de Datos Híbrida Inteligente**:
  - `DEBUG = True`: Usa **SQLite** local para desarrollo rápido.
  - `DEBUG = False`: Se conecta a **Neon Tech PostgreSQL** en producción.

---

## 🛠️ Requisitos Previos

- Python 3.10+
- Pip / virtualenv

---

## 🚀 Instalación y Ejecución Local

1. **Clonar el repositorio**:
   ```bash
   git clone <URL_DE_TU_REPOSITORIO>
   cd app-cuestionarios
   ```

2. **Instalar dependencias**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Ejecutar migraciones en la base de datos local**:
   ```bash
   python manage.py migrate
   ```

4. **Poblar las 30 preguntas iniciales del documento PDF**:
   ```bash
   python manage.py seed_preguntas
   ```

5. **Crear usuario administrador**:
   ```bash
   python manage.py createsuperuser
   ```

6. **Iniciar el servidor local**:
   ```bash
   python manage.py runserver
   ```
   - **Evaluaciones**: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
   - **Panel Admin**: [http://127.0.0.1:8000/panel-admin/](http://127.0.0.1:8000/panel-admin/)

---

## ☁️ Despliegue en Vercel

El proyecto incluye los archivos preconfigurados para Vercel:
- `vercel.json`
- `build_files.sh`

### Pasos para desplegar:
1. Sube tu código a un repositorio de **GitHub / GitLab**.
2. Conecta tu cuenta en **Vercel** e importa el proyecto.
3. En la sección **Environment Variables**, añade:
   - `DEBUG` = `False`
   - `DATABASE_URL` = `postgresql://neondb_owner:npg_Esjfu8kSR9Kx@ep-morning-hat-ayib960a.c-5.us-east-2.aws.neon.tech/neondb?sslmode=require`
   - `SECRET_KEY` = `tu_clave_secreta_de_django`
4. Haz clic en **Deploy**.

---

## 👨‍💻 Autor

Desarrollado por **Victor Molina**
