from django.core.management.base import BaseCommand
from cuestionario.models import Pregunta

QUESTIONS_DATA = [
    # GENERAL / MANUAL OPERATIVO PARA CONDUCTORES
    {
        'categoria': 'MANUAL OPERATIVO PARA CONDUCTORES',
        'texto': '¿Qué debe hacer el conductor antes de realizar un viaje?',
        'opcion_a': 'Esperar la autorización del cliente.',
        'opcion_b': 'Realizar la inspección visual diaria y guardar el reporte.',
        'opcion_c': 'Revisar únicamente el nivel de combustible.',
        'opcion_d': 'Comunicarse únicamente con el guardia de planta.',
        'opcion_correcta': 'B'
    },
    {
        'categoria': 'MANUAL OPERATIVO PARA CONDUCTORES',
        'texto': 'En la inspección visual, ¿qué significa que una unidad aparezca en color rojo?',
        'opcion_a': 'La unidad está operativa y puede viajar.',
        'opcion_b': 'La unidad requiere mantenimiento, pero puede viajar.',
        'opcion_c': 'La unidad no está operativa.',
        'opcion_d': 'La unidad está disponible para cualquier conductor.',
        'opcion_correcta': 'C'
    },
    {
        'categoria': 'MANUAL OPERATIVO PARA CONDUCTORES',
        'texto': '¿Cuál es la velocidad máxima permitida en ruta para las unidades?',
        'opcion_a': '50 km/h.',
        'opcion_b': '60 km/h.',
        'opcion_c': '70 km/h.',
        'opcion_d': '80 km/h.',
        'opcion_correcta': 'C'
    },
    {
        'categoria': 'MANUAL OPERATIVO PARA CONDUCTORES',
        'texto': 'Antes de salir de planta, ¿qué debe verificar el conductor respecto a los bines y materiales?',
        'opcion_a': 'Que la cantidad de bines sea aproximada a la guía.',
        'opcion_b': 'Que la numeración de los bines y los materiales coincidan con la guía.',
        'opcion_c': 'Que los bines estén vacíos.',
        'opcion_d': 'Que el cliente confirme la carga por teléfono.',
        'opcion_correcta': 'B'
    },
    {
        'categoria': 'MANUAL OPERATIVO PARA CONDUCTORES',
        'texto': '¿Cuándo puede salir la unidad de planta?',
        'opcion_a': 'Cuando el conductor considere que está lista.',
        'opcion_b': 'Cuando haya terminado de cargar, aunque falten firmas.',
        'opcion_c': 'Cuando garita confirme que la guía, firmas, sellos y carga física coinciden.',
        'opcion_d': 'Cuando el cliente autorice la salida.',
        'opcion_correcta': 'C'
    },
    {
        'categoria': 'MANUAL OPERATIVO PARA CONDUCTORES',
        'texto': 'Al finalizar una pesca, ¿qué debe hacer el conductor con la guía de transportista?',
        'opcion_a': 'Botarla después de tomarle una foto.',
        'opcion_b': 'Entregarla inmediatamente al cliente.',
        'opcion_c': 'Tomar una foto, enviarla al grupo Reporte Distrilógico, conservarla durante la ruta y entregarla físicamente para el cierre.',
        'opcion_d': 'Guardarla hasta finalizar el mes.',
        'opcion_correcta': 'C'
    },
    {
        'categoria': 'MANUAL OPERATIVO PARA CONDUCTORES',
        'texto': 'Para cargar diésel, ¿qué debe hacer primero el conductor?',
        'opcion_a': 'Dirigirse directamente a cualquier gasolinera.',
        'opcion_b': 'Solicitar autorización al Call Center Distrilógico.',
        'opcion_c': 'Pedir autorización al guardia de planta.',
        'opcion_d': 'Cargar primero y reportarlo después.',
        'opcion_correcta': 'B'
    },
    {
        'categoria': 'MANUAL OPERATIVO PARA CONDUCTORES',
        'texto': 'Si la unidad presenta una falla mecánica o eléctrica, ¿qué debe hacer el conductor?',
        'opcion_a': 'Continuar trabajando hasta que la falla empeore.',
        'opcion_b': 'Llevar la unidad directamente al taller sin cita.',
        'opcion_c': 'Solicitar turno de taller y comunicar la novedad correspondiente.',
        'opcion_d': 'Esperar al siguiente mantenimiento programado.',
        'opcion_correcta': 'C'
    },
    {
        'categoria': 'MANUAL OPERATIVO PARA CONDUCTORES',
        'texto': '¿Qué debe hacer el conductor ante un accidente, robo, incendio o emergencia?',
        'opcion_a': 'Continuar el viaje si la unidad todavía funciona.',
        'opcion_b': 'Esperar instrucciones del cliente antes de reportar.',
        'opcion_c': 'Priorizar su seguridad, llamar al 911 si es necesario y reportar inmediatamente a la empresa.',
        'opcion_d': 'Resolver la situación por cuenta propia.',
        'opcion_correcta': 'C'
    },
    {
        'categoria': 'MANUAL OPERATIVO PARA CONDUCTORES',
        'texto': '¿Qué debe hacer el conductor si necesita realizar un movimiento fuera de la ruta establecida?',
        'opcion_a': 'Realizarlo si considera que es necesario.',
        'opcion_b': 'Informarlo después de completar el viaje.',
        'opcion_c': 'Solicitar autorización al coordinador de turno.',
        'opcion_d': 'Consultarlo únicamente con otro conductor.',
        'opcion_correcta': 'C'
    },

    # MÓDULO 1: MANUAL OPERATIVO DE PESCA VIVA
    {
        'categoria': 'MÓDULO 1: MANUAL OPERATIVO DE PESCA VIVA',
        'texto': 'Antes de salir hacia la camaronera, ¿qué porcentaje mínimo de carga debe tener el termo de oxígeno?',
        'opcion_a': '20%',
        'opcion_b': '30%',
        'opcion_c': 'Más del 50%',
        'opcion_d': '100% siempre',
        'opcion_correcta': 'C'
    },
    {
        'categoria': 'MÓDULO 1: MANUAL OPERATIVO DE PESCA VIVA',
        'texto': '¿Cuántas mallas internas debe tener cada bin?',
        'opcion_a': '2 mallas',
        'opcion_b': '3 mallas',
        'opcion_c': '4 mallas',
        'opcion_d': '5 mallas',
        'opcion_correcta': 'C'
    },
    {
        'categoria': 'MÓDULO 1: MANUAL OPERATIVO DE PESCA VIVA',
        'texto': '¿Qué elementos deben revisarse antes de salir a la camaronera?',
        'opcion_a': 'Solo el combustible de la unidad.',
        'opcion_b': 'Spiga, rackkor, mangueras y flauta.',
        'opcion_c': 'Solo las gavetas.',
        'opcion_d': 'Únicamente los bines.',
        'opcion_correcta': 'B'
    },
    {
        'categoria': 'MÓDULO 1: MANUAL OPERATIVO DE PESCA VIVA',
        'texto': '¿Cómo debe asegurarse el termo de oxígeno en la plataforma?',
        'opcion_a': 'Con una cuerda suelta.',
        'opcion_b': 'Con cinta adhesiva.',
        'opcion_c': 'Con ratchet o cabo.',
        'opcion_d': 'No es necesario asegurarlo.',
        'opcion_correcta': 'C'
    },
    {
        'categoria': 'MÓDULO 1: MANUAL OPERATIVO DE PESCA VIVA',
        'texto': '¿Quién determina la saturación requerida para cada bin durante la pesca viva?',
        'opcion_a': 'El conductor.',
        'opcion_b': 'El guardia de la camaronera.',
        'opcion_c': 'El parametrista.',
        'opcion_d': 'El personal de bodega.',
        'opcion_correcta': 'C'
    },
    {
        'categoria': 'MÓDULO 1: MANUAL OPERATIVO DE PESCA VIVA',
        'texto': '¿A qué presión debe regularse el termo de oxígeno antes de la cosecha?',
        'opcion_a': '20 PSI',
        'opcion_b': '30 PSI',
        'opcion_c': '50 PSI',
        'opcion_d': '100 PSI',
        'opcion_correcta': 'D'
    },
    {
        'categoria': 'MÓDULO 1: MANUAL OPERATIVO DE PESCA VIVA',
        'texto': '¿Cuál es el rango de presión indicado para la válvula de gas/oxígeno?',
        'opcion_a': '5 a 10 PSI',
        'opcion_b': '10 a 15 PSI',
        'opcion_c': '20 a 30 PSI',
        'opcion_d': '40 a 50 PSI',
        'opcion_correcta': 'C'
    },
    {
        'categoria': 'MÓDULO 1: MANUAL OPERATIVO DE PESCA VIVA',
        'texto': 'Durante el traslado, ¿qué debe hacer el conductor con los bines?',
        'opcion_a': 'Mantenerlos presurizados.',
        'opcion_b': 'Vaciarles la presión.',
        'opcion_c': 'Desconectar las mangueras.',
        'opcion_d': 'Cerrar inmediatamente la válvula constructora.',
        'opcion_correcta': 'A'
    },
    {
        'categoria': 'MÓDULO 1: MANUAL OPERATIVO DE PESCA VIVA',
        'texto': '¿Qué debe hacer el conductor una vez finalizada la descarga de la pesca viva?',
        'opcion_a': 'Retirarse inmediatamente de la planta.',
        'opcion_b': 'Cerrar las válvulas del termo y descargar y ordenar los equipos utilizados.',
        'opcion_c': 'Dejar los equipos dentro de la unidad.',
        'opcion_d': 'Mantener las válvulas abiertas.',
        'opcion_correcta': 'B'
    },
    {
        'categoria': 'MÓDULO 1: MANUAL OPERATIVO DE PESCA VIVA',
        'texto': 'Antes de movilizarse hacia el área de recepción, ¿qué debe hacer el conductor con los sacos vacíos?',
        'opcion_a': 'Dejarlos sueltos en la unidad.',
        'opcion_b': 'Colocarlos sobre los bines.',
        'opcion_c': 'Amarrarlos correctamente utilizando el cabo.',
        'opcion_d': 'Entregarlos antes de salir.',
        'opcion_correcta': 'C'
    },

    # MÓDULO 2: MANUAL DE SEGURIDAD - PLANTA LIMBOPACK
    {
        'categoria': 'MÓDULO 2: MANUAL DE SEGURIDAD - PLANTA LIMBOPACK',
        'texto': '¿Qué equipos de protección personal debe utilizar el conductor para ingresar a Planta Limbopack?',
        'opcion_a': 'Solo casco.',
        'opcion_b': 'Casco, chaleco reflectivo, botas de seguridad y demás EPP requeridos.',
        'opcion_c': 'Solo chaleco reflectivo.',
        'opcion_d': 'Solo botas de seguridad.',
        'opcion_correcta': 'B'
    },
    {
        'categoria': 'MÓDULO 2: MANUAL DE SEGURIDAD - PLANTA LIMBOPACK',
        'texto': '¿Cuál es la velocidad máxima permitida dentro de Planta Limbopack?',
        'opcion_a': '10 km/h',
        'opcion_b': '15 km/h',
        'opcion_c': '20 km/h',
        'opcion_d': '30 km/h',
        'opcion_correcta': 'C'
    },
    {
        'categoria': 'MÓDULO 2: MANUAL DE SEGURIDAD - PLANTA LIMBOPACK',
        'texto': '¿Qué está prohibido hacer dentro de las instalaciones de Limbopack?',
        'opcion_a': 'Utilizar el paso peatonal.',
        'opcion_b': 'Utilizar el casco.',
        'opcion_c': 'Pitar.',
        'opcion_d': 'Presentar la guía.',
        'opcion_correcta': 'C'
    },
    {
        'categoria': 'MÓDULO 2: MANUAL DE SEGURIDAD - PLANTA LIMBOPACK',
        'texto': 'Al caminar dentro de la planta para entregar la guía, ¿por dónde debe transitar el conductor?',
        'opcion_a': 'Por cualquier área disponible.',
        'opcion_b': 'Por el área destinada para paso peatonal.',
        'opcion_c': 'Por el área de descarga.',
        'opcion_d': 'Por detrás de las unidades.',
        'opcion_correcta': 'B'
    },
    {
        'categoria': 'MÓDULO 2: MANUAL DE SEGURIDAD - PLANTA LIMBOPACK',
        'texto': 'Mientras espera que el área de recepción lo llame para descargar el producto, ¿dónde debe permanecer el conductor?',
        'opcion_a': 'Fuera de la unidad.',
        'opcion_b': 'En la garita.',
        'opcion_c': 'Dentro de la unidad.',
        'opcion_d': 'En el área de descarga.',
        'opcion_correcta': 'C'
    },
    {
        'categoria': 'MÓDULO 2: MANUAL DE SEGURIDAD - PLANTA LIMBOPACK',
        'texto': '¿Cuándo puede el conductor bajarse de la unidad durante el proceso de carga o descarga?',
        'opcion_a': 'Cuando quiera revisar la planta.',
        'opcion_b': 'Únicamente cuando sea necesario y utilizando los equipos de seguridad correspondientes.',
        'opcion_c': 'Siempre que esté esperando.',
        'opcion_d': 'Nunca puede bajarse.',
        'opcion_correcta': 'B'
    },
    {
        'categoria': 'MÓDULO 2: MANUAL DE SEGURIDAD - PLANTA LIMBOPACK',
        'texto': 'Antes de iniciar las labores el día domingo, ¿qué nivel mínimo de combustible debe tener la unidad?',
        'opcion_a': '1/4 de tanque.',
        'opcion_b': '1/2 tanque.',
        'opcion_c': '3/4 de tanque.',
        'opcion_d': 'Tanque completamente lleno.',
        'opcion_correcta': 'C'
    },
    {
        'categoria': 'MÓDULO 2: MANUAL DE SEGURIDAD - PLANTA LIMBOPACK',
        'texto': 'Si el conductor detecta un desperfecto en la unidad, ¿qué debe hacer?',
        'opcion_a': 'Continuar trabajando hasta terminar el viaje.',
        'opcion_b': 'Repararlo personalmente.',
        'opcion_c': 'Informar al coordinador de turno para coordinar la salida a taller.',
        'opcion_d': 'Esperar al siguiente mantenimiento.',
        'opcion_correcta': 'C'
    },
    {
        'categoria': 'MÓDULO 2: MANUAL DE SEGURIDAD - PLANTA LIMBOPACK',
        'texto': 'Si el conductor presenta una novedad o eventualidad durante la operación, ¿a quién debe comunicarla?',
        'opcion_a': 'A otro conductor.',
        'opcion_b': 'Al coordinador de turno en Limbopack.',
        'opcion_c': 'Únicamente al cliente.',
        'opcion_d': 'No es necesario reportarla.',
        'opcion_correcta': 'B'
    },
    {
        'categoria': 'MÓDULO 2: MANUAL DE SEGURIDAD - PLANTA LIMBOPACK',
        'texto': '¿Cuál de las siguientes opciones forma parte de la lista de verificación rápida antes de la operación?',
        'opcion_a': 'Equipo de seguridad completo, combustible verificado, estado de la unidad y guía preparada.',
        'opcion_b': 'Solo revisar el combustible.',
        'opcion_c': 'Revisar únicamente la guía de transporte.',
        'opcion_d': 'Verificar únicamente la ruta.',
        'opcion_correcta': 'A'
    }
]

class Command(BaseCommand):
    help = 'Carga las 30 preguntas iniciales del PDF en la base de datos Neon PostgreSQL'

    def handle(self, *args, **options):
        self.stdout.write('Iniciando sembrado de preguntas...')
        created_count = 0
        updated_count = 0

        for q in QUESTIONS_DATA:
            obj, created = Pregunta.objects.get_or_create(
                texto=q['texto'],
                defaults={
                    'categoria': q['categoria'],
                    'opcion_a': q['opcion_a'],
                    'opcion_b': q['opcion_b'],
                    'opcion_c': q['opcion_c'],
                    'opcion_d': q['opcion_d'],
                    'opcion_correcta': q['opcion_correcta'],
                    'activa': True
                }
            )
            if created:
                created_count += 1
            else:
                updated_count += 1

        self.stdout.write(self.style.SUCCESS(
            f'Sembrado completado exitosamente: {created_count} preguntas creadas, {updated_count} existentes.'
        ))
