# FastAPI-JWT-SQLAlchemy
Este proyecto se realizo con la intención de entender el funcionamiento del framework de FastAPI y de la herramienta de SQLAlchemy y JWT. 
Se trabajo con un crud sencillo con dos modelos implementados que son user y task que estan relacionadas. En el modelo de user se implemento 
JWT para tener una autenticacion del usuario por medio de un token que se genera.
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
 └─── requirements.txt
```
