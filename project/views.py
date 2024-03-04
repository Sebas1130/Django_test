from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string
from xhtml2pdf import pisa
import boto3
from botocore.exceptions import NoCredentialsError

from .models import Producto
# Create your views here.

# Vista de inventario
def inventario_view(request):
    # Obtener todos los productos de la base de datos
    productos = Producto.objects.all()

    if request.method == 'POST':
        # Generar PDF
        pdf_data = generar_pdf(productos)

        # Enviar PDF por correo electrónico
        enviar_correo(pdf_data)

        return HttpResponse("Correo enviado con éxito")

    return render(request, 'inventario.html', {'productos': productos})

def generar_pdf(inventario_data):
    # Renderizar la plantilla HTML con la información del inventario
    html = render_to_string('inventario_pdf_template.html', {'inventario_data': inventario_data})

    # Crear un archivo PDF
    pdf = BytesIO()
    pisa.CreatePDF(html, dest=pdf)

    return pdf.getvalue()

def enviar_correo(pdf_data):
    # Configurar cliente de Amazon SES
    ses = boto3.client('ses', region_name='us-east-1', aws_access_key_id='your-access-key-id', aws_secret_access_key='your-secret-access-key')

    # Construir el correo electrónico
    email_subject = "Informe de inventario"
    email_body = "Adjunto encontrarás el informe de inventario."
    sender_email = "your-sender-email@example.com"
    recipient_email = "recipient-email@example.com"

    # Enviar correo electrónico con el PDF adjunto
    try:
        ses.send_email(
            Source=sender_email,
            Destination={'ToAddresses': [recipient_email]},
            Message={
                'Subject': {'Data': email_subject},
                'Body': {'Text': {'Data': email_body}},
                'Attachments': [
                    {
                        'FileName': 'inventario.pdf',
                        'Data': pdf_data,
                        'ContentType': 'application/pdf'
                    }
                ]
            }
        )
    except NoCredentialsError:
        return "Credenciales de AWS no encontradas"
