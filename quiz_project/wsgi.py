import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'quiz_project.settings')

application = get_wsgi_application()
app = application

# Auto-ejecución de migraciones y sembrado de preguntas al iniciar en Vercel
if os.environ.get('VERCEL') == '1' or os.environ.get('VERCEL_ENV'):
    try:
        from django.core.management import call_command
        print("Ejecutando migraciones automáticas en Neon Tech...")
        call_command('migrate', interactive=False)
        print("Ejecutando sembrado de preguntas...")
        call_command('seed_preguntas')
    except Exception as e:
        print("Error durante la inicialización en Vercel:", e)
