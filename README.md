# README para Backend en Flask con PostgreSQL

## Descripción General

Este proyecto es un backend desarrollado en Python utilizando el framework Flask. Está diseñado para gestionar empleados y sus entradas/salidas de una empresa. Utiliza PostgreSQL como sistema de gestión de base de datos, corriendo en un contenedor Docker para facilitar la configuración y el despliegue.

## Estructura Modular

El proyecto está organizado de manera modular para facilitar la mantenibilidad y escalabilidad del código:

- **`models/`**: Contiene las clases que representan las entidades de la base de datos.
- **`services/`**: Capa de servicio que contiene la lógica de negocio y las interacciones con la base de datos.
- **`controllers/`**: Controladores que manejan las solicitudes HTTP, interactúan con la capa de servicio y devuelven respuestas al cliente.
- **`routes/`**: Define las rutas HTTP que están disponibles en la API y vincula estas rutas con sus controladores correspondientes.

## Funciones del Programa

- **Registro de empleados**: Permite registrar nuevos empleados en el sistema.
- **Registro de entradas y salidas**: Gestiona las marcas de tiempo de entrada y salida de los empleados.
- **Consulta de empleados**: Permite obtener una lista de todos los empleados registrados.
- **Consulta de entradas/salidas**: Permite obtener todas las entradas y salidas registradas.
- **Cálculo de tiempo total**: Calcula el tiempo total que un empleado ha pasado en las instalaciones en una fecha específica.

## Requisitos

Para ejecutar este proyecto, necesitarás Python y pip para instalar las dependencias, que están listadas en el archivo `requirements.txt`. Además, es necesario tener Docker instalado si deseas ejecutar la base de datos PostgreSQL en un contenedor.

## Configuración

### Base de Datos

Este proyecto utiliza PostgreSQL. Se recomienda ejecutar PostgreSQL dentro de un contenedor Docker. Puedes iniciar un contenedor con PostgreSQL usando el siguiente comando:

```bash
docker run --name postgresql-container -p 5432:5432 -e POSTGRES_USER=miusuario -e POSTGRES_PASSWORD=mipassword -d postgres
```

### Archivo `.env`

Debes crear un archivo `.env` en el directorio raíz del proyecto para almacenar las variables de entorno necesarias para la configuración. Este archivo debe contener detalles como el nombre de usuario, contraseña, host y nombre de la base de datos. Ejemplo:

## Ejecución

Para ejecutar el proyecto, primero instala las dependencias:
```bash
pip install -r requirements.txt
```


Luego, puedes iniciar el servidor Flask ejecutando:
```bash
python app.py
```

## Recuperar Datos Dummy

Si deseas recuperar los datos dummy utilizando el volcado de la base de datos (`pg_dump`), sigue estos pasos:

1. **Copia el archivo de volcado a tu contenedor Docker**:
```bash
docker cp ./control_ingreso.dump postgresql-container:/tmp/control_ingreso.dump
```

2. **Restaurar el volcado en la base de datos**:
    - `postgresql-container`: Nombre del contenedor Docker.
    - `miusuario`: Usuario de la base de datos.
    - `midatabase`: Nombre de la base de datos donde se restaurarán los datos.
    - `/tmp/control_ingreso.dump`: Ruta dentro del contenedor donde se encuentra el archivo de volcado.
