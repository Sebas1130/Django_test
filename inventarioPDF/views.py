import os
from io import BytesIO
from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string
from xhtml2pdf import pisa
import boto3
from botocore.exceptions import NoCredentialsError

# Importaciones del modelo
from project.models import Producto

# Importaciones para cargar variables de entorno
#from dotenv import load_dotenv
#from os import getenv


# Configurar cliente de Amazon SNS
#load_dotenv()
sns_client = boto3.client("sns",
                        aws_access_key_id=os.environ.get("AWS_ACCESS_KEY_ID"),
                        aws_secret_access_key=os.environ.get("AWS_SECRET_ACCESS_KEY"),
                        region_name=os.environ.get("AWS_REGION"))


# Vista de inventario
def enviar_pdf_correo(request):
    if request.method == 'POST':
        # Obtener todos los productos de la base de datos
        productos = Producto.objects.all()

        # Generar el PDF
        pdf_data = generar_pdf(productos)

        # Obtener el asunto y el correo electrónico del destinatario del formulario
        email_subject = request.POST.get('subject')
        recipient_email = request.POST.get('recipient_email')

        # Enviar el correo electrónico con el PDF adjunto
        enviar_correo(email_subject, recipient_email, pdf_data)

        return HttpResponse("Correo enviado con éxito")

    return render(request, 'inventario.html')

def generar_pdf(productos):
    # Renderizar la plantilla HTML con los datos de los productos
    html = render_to_string('productos_pdf_template.html', {'productos': productos})

    # Crear un archivo PDF
    pdf = BytesIO()
    pisa.CreatePDF(html, dest=pdf)

    return pdf.getvalue()

def enviar_correo(email_subject, recipient_email, pdf_data):
    # Enviar correo electrónico con el PDF adjunto
    try:
        sns_client.publish(
            TopicArn="arn:aws:sns:us-east-1:992565669267:Inventario",
            Message=email_subject,
            Subject="Informe de inventario",
            MessageStructure="string",
            MessageAttributes={
                'email_body': {
                    'DataType': 'String',
                    'StringValue': "Adjunto encontrarás el informe de inventario."
                },
                'pdf_attachment': {
                    'DataType': 'Binary',
                    'BinaryValue': pdf_data
                }
            }
        )
        return "Correo enviado con éxito"
    except NoCredentialsError:
        return "Credenciales de AWS no encontradas"


def suscribir_cliente_view(request):
    if request.method == 'POST':
        email_subject = request.POST.get('email_subject')

        # Suscribir correo para mandar Email
        try:
            response = sns_client.subscribe(
                TopicArn="arn:aws:sns:us-east-1:992565669267:Inventario",
                Protocol="email",
                Endpoint=email_subject,
                ReturnSubscriptionArn=True
            )
            print(response)
            return HttpResponse("Correo suscrito con éxito")
        except:
            return HttpResponse("Error al suscribir el correo electrónico")

    return render(request, 'formulario_suscripcion.html')
