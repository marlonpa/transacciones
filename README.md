# transacciones
APP para transacciones por cliente

Paso para correr el la aplicacion
Se instala python y agregamos las variables de entorno de python
Creacion de entorno virtual

$ mkdir entorno $ cd entorno $ python -m venv "nombre entorno"

Activar entorno
$source "nombre entorno"/bin/activate

Instalar pip en el entorno
$python -m pip install --upgrade pip

Clonamos el proyecto
$git clone 'https://github.com/marlonpa/transacciones.git'

Instalar dependencias
$pip install -r requirements.txt

Se crea base de datos en mysql
mysql -u root -p 
create database transacciones;

Corremos el proyecto
$python manager.py makemigrations users transaccion
$python manager.py migrate 
$python manager.py createsuperuser 
$python manager.py runserver

Abrimos navegador
localhost:8000

para consultar la api
localhost:8000/list

para paginar: ?page=1

para filtrar: ?search=
