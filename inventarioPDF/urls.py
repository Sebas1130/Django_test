from django.urls import path
from . import views

urlpatterns = [
    path('enviar_pdf_correo/', views.enviar_pdf_correo, name='enviar_pdf_correo'),
    path('subcliente/', views.suscribir_cliente_view, name='subcliente'),
]