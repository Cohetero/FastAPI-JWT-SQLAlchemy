# FastAPI-JWT-SQLAlchemy
Este proyecto se realizo con la intención de entender el funcionamiento del framework de FastAPI y de la herramienta de SQLAlchemy y JWT. 
Se trabajo con un crud sencillo con dos modelos implementados que son user y task que estan relacionadas. En el modelo de user se implemento 
JWT para tener una autenticacion del usuario por medio de un token que se genera. El proyecto consiste en donde se registran usuarios y valida si el usuario y/o correo existen para ser registrados, una vez registrados se le da un token para acceder y agregar sus tareas o verlas, Asi mismo se puede administrar los usuarios a traves de un CRUD. El proyecto esta hecho en python.
## Contenido
- Estructura del código
- Modelos
- Variables de entorno
- <details><summary>Correr el Proyecto via Docker</summary>
    <ul>
      <li> Instalar docker</li>
      <li> Construir docker-compose</li>
      <li> Servicios de docker</li>
      <li> Ejecutar docker-compose</li>
    </ul>
  </details>
- <details><summary>Correr el Proyecto via entorno virtual</summary>
    <ul>
      <li> Crear un entorno virtual</li>
      <li> Instalar el archivo de requirements.txt</li>
      <li> Ejecutar el proyecto</li>
    </ul>
  </details>
  
## Estructura del código
```
 FastAPI-JWT-SQLAlchemy
 ├─── app
 |   └─── v1
 |        ├─── model
 |        |    ├─── task_model.py
 |        |    └─── user_model.py
 |        ├─── router
 |        |    ├─── task_router.py
 |        |    └─── user_router.py
 |        ├─── schema
 |        |    ├─── task_chema.py
 |        |    ├─── toke_schema.py
 |        |    └─── user_schema.py
 |        ├─── scripts
 |        |    └─── create_tables.py
 |        ├─── service
 |        |    ├─── auth_service.py
 |        |    ├─── task_service.py
 |        |    └─── user_service.py
 |        └─── utils
 |             ├─── db.py
 |             └─── settings.py
 ├─── .gitignore
 ├─── docker-compose.yml
 ├─── Dockerfile
 ├─── main.py
 ├─── .env
 └─── requirements.txt
```
Como se ve en la estructura estan dividos los archivos en sus carpetas que se corresponden e igual estan nombrados en la carpeta que estan, esto se hizo mas que nada para evitar confusiones entre los archivos a la hora de ser llamados.

## Modelos
La aplicación implemente 2 modelos para almacenar la información de usuarios y las tareas que se les agrega a cada usuario
- **User**: Guarda la información de los usuarios que se registran, que son username, email y password
- **Task**: Guarda las tareas que va a realizar el usuario que le corresponda. Guarda el nombre de la tarea, la fecha de creación, si se ha realizado o no y el id del usuario que le corresponde dicha tarea.

## Variables de entorno
Antes que nada se tiene que crear el archivo de **.env** en la rais del proyecto (junto con main.py) uba vez creado el archvio, las variables de entorno que se tiene que tomar en cuenta son las siguientes

```
# Database connection
DB_NAME = name_database
DB_USER = user
DB_PASS = password
DB_HOST = host
DB_PORT = port

# Auth
ACCESS_TOKEN_EXPIRE_MINUTES = tiempo_en_que_expira_el_token
SECRET_KEY = clave
```
para obtener la clave, en linux ejecute el siguiente comando
```
openssl rand -hex 32
```
la clave es para codificar y decodificar nuestros tokens. Para acceder a ellos solo es instalando el archvo de requeriments.txt que trate el paquete de python-dotenv que nos ayuda a obtener esas variables de entorno en nuestro proyecto

## Correr el Proyecto via Docker
Para correr el proyecto en docker es sencillo

### Instalar docker
Para instalar docker y docker compose, les dijo los siguientes links:
1. Instalar docker [Docker](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-20-04-es)
2. Instalar docker-compose [Docker-Compose](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-compose-on-ubuntu-20-04-es)

### Construir docker-compose
Para construir docker-compose solo ejecute el siguiente comando dentro de la carpeta de app
```
docker-compose build
o
sudo docker-compose build
```

### Servicios de docker
Docker-compose solo cuenta con dos servicios:
- **fast-api**: Que es el servicio de ejecutar el proyecto, donde tiene un comando que indica que se ejecute el proyecto y como quiere ser ejecutado, un volumen, el port donde hace la conexion entre docker y el proyecto y depende del servicio de postgres para ejecutarse
- **postgres**: Es el servicio de la base de datos, que es postgres. Donde tiene la imagen mas reciente, tiene un volumen para guardar la base de datos, unas variables de entorno para conectar a la base de datos y corre en el puerto de 5432

### Ejecutar docker-compose
Para ejecutar docker-compose es sencillo, una vez que ya se construyo se ejecuta los siguientes comandos:
```
# Correrlo normal
docker-compose up

# Correrlo en segundo plano
docker-compose up -d

# Correr algun servicio especifio
docker-compose up service

# Terminar docker-compose si esta en segundo plano
docker-compose down

# Terminar docker-compose si no esta en segundo plano
ctrl + c
```


## Correr el Proyecto via entorno virtual
Para correrlo en un ambiente virtual es sencillo

### Crear un entorno virtual
Para crear el entorno virtual hay de diferentes maneras, en este caso lo explicare con virtualenv. Para instalarlo ejecuta el siguiente comando:
```
pip3 install virtualenv
```
Para crear el entorno virtual
```
virtualenv -p python3 nombreVirtual
```
Para ejecutarlo y desactivarlo
```
# Windows
. nombreVirtual/Scripts/activate

# inux
. nombreVirtual/bin/activate

# Para desactivarlo
deactivate
```
### Instalar el archivo de requirements.txt
Se tiene que instalar, dentro del entorno virtual, los paquetes que tiene requirements.txt para poder ejecutar el proyecto
```
pip install -r requirements.txt
```
### Ejecutar el proyecto
Para ejecutar el proyecto hay de dos formas, al nivel del archivo main.py
```
# SOlo ejecutando el archivo main.py
python3 main.py

# Ejecutarlo con uvicorn
uvicorn main:app --port 5000 --reload
```
