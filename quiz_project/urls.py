from django.contrib import admin
from django.urls import path
from cuestionario import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Rutas Públicas para Evaluados
    path('', views.inicio_view, name='inicio'),
    path('cuestionario/', views.cuestionario_view, name='cuestionario_evaluacion'),
    path('resultado/<int:intento_id>/', views.resultado_view, name='resultado_evaluacion'),

    # Rutas del Panel de Administración Personalizado
    path('panel-admin/login/', views.admin_login_view, name='admin_login'),
    path('panel-admin/logout/', views.admin_logout_view, name='admin_logout'),
    path('panel-admin/', views.admin_dashboard_view, name='admin_dashboard'),
    path('panel-admin/intento/<int:intento_id>/', views.admin_intento_detalle_view, name='admin_intento_detalle'),
    path('panel-admin/exportar-excel/', views.admin_exportar_excel_view, name='admin_exportar_excel'),
    path('panel-admin/importar-excel/', views.admin_importar_excel_view, name='admin_importar_excel'),
    path('panel-admin/descargar-plantilla/', views.admin_descargar_plantilla_view, name='admin_descargar_plantilla'),
    path('panel-admin/preguntas/', views.admin_preguntas_list_view, name='admin_preguntas_list'),
]
