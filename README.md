# django-CRUD
Una aplicación sencilla construida con Django cuanta con tres módulos 'inventarioPDF','registry','project' en los cuales todos manejan sus rutas por separados.

En el módulo 'project' se encuentran definidos los modelos para interactuar con la DB-postgres, cuenta con 5 modelos 'Categoría','Producto','Cliente','Orden','OrdenProducto' los cuales todo cuentan con su CRUD realizado a través de django rest framework

En el modulo 'registry' se encuentran definidas las rutas de login,sign in,signup los cuales se autentican por medio de token para definir a qué vistas del home pueden acceder y a cuáles no sin autorización

En el modulo 'inventarioPDF' se realiza todo el envío y registro del email adjuntando todo lo que tenga en el inventario que sería el modelo de Producto en donde se traen todos los datos de esta tabla y se envía al correo seleccionado


### Setup
Actualizar el sistema
```bash
sudo apt-get update
```
Para obtener este repositorio, ejecute el siguiente comando dentro de su terminal habilitada para git
```bash
git clone https://github.com/Sebas1130/Django_test.git
```
Antes de corrre la aplicacion se tiene que instalar el docker-compose
```bash
sudo apt install docker-compose
```
Tambien toca agregarles los valores a los archivos .enviroments/aws/config
```bash
AWS_ACCESS_KEY_ID=''
AWS_SECRET_ACCESS_KEY=''
AWS_REGION='us-east-1'
```
Despues toca configurar los env Asegúrate de tener privilegios de superusuario o estar en el grupo docker:
```bash
groups
sudo usermod -aG docker $USER
sudo service docker restart
ls -l /var/run/docker.sock
sudo chmod 666 /var/run/docker.sock
```

Despues debes copiar el archivo requeriments.txt en la ruta donde lo busca el Dockerfile
```bash
cp /home/ubuntu/Django_test/requirements.txt /home/ubuntu/Django_test/compose/dev/django/
```

listo ya despues solo haces los comandos de ejecucion del proyecto
```bash
export COMPOSE_FILE=local.yml; docker-compose build
```
```bash
export COMPOSE_FILE=local.yml; docker-compose up
```

Una vez que el servidor esté hosted dirígete a http://0.0.0.0:8000 para ver la aplicacion

Saludos y feliz codificación :)
