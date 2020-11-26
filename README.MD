# Proyecto Back end Team - Django - Prueba técnica

- Teniendo un entorno Windows

## 1) Instalacion de Python, Django, Entorno virtual y BBDD

- Descargamos e instalamos Python del siguiente [enlace](https://www.python.org/downloads/)
- Instalamos `pip` siguiendo los pasos de este [enlace](https://www.neoguias.com/como-instalar-pip-python/)
- Instalamos postgresql siguiendo los pasos de este [enlace](https://www.solvetic.com/tutoriales/article/7676-como-instalar-postgresql-en-windows-10/)
- Instalamos el entorno virtual desde nuestro cmd `pip install virtualenv`
- Levantamos el entorno virtual desde la raiz de nuestro proyecto `Scripts\activate.bat`
- Una vez dentro del entorno virtual instalamos todas las dependencias del proyecto: `pip install -r requirements.txt`
- Recuerda configurar las credenciales de tu base de datos en el archivo `aguacate\settings.py`
- Tenemos que ejecutar las migraciones con los comandos `python manage.py makemigrations` y `python manage.py migrate`
- Para levantar el servidor ejecutamos `python manage.py runserver`
- Y ya tendriamos nuestra API en funcionamiento

## 2) Observación

### 2.1) Funcionamiento de la API
| URL | Método | Parámetros | Descripción |
|---|---|---|---|
| `register` | `POST` | NULL | Crear un nuevo usuario |
| `createidea/` | `POST` | NULL | Crear una nueva idea |
| `updateidea/` | PUT | `<int:idea_id>` | Modifica los valores de una idea, (visibilidad, texto, fecha) |
| `listorderidea/` | GET | NULL | Devuelve todas las ideas ordenadas por fecha |
| `deleteidea/` | DELETE | <int:idea_id> | Elimina una idea |
| `solicitud/` | PUT | <int:idea_id> | Registra una solicitud de seguimiento de usuario |  
| `listinvitation` | GET | NULL | Devuelve todas las invitaciones realizadas |
| `updateinvitation` | PUT | `<int:invitation_id>` | Modifica el status de una invitacion |
| `listfollowers/` | GET | NULL | Devuelve los seguidores del usuario |
| `listfollowing/` | GET | NULL | Devuelve los seguidores de un usuario |
| `deleteinvitation/` | DELETE | <int:invitation_id> | Elimina una solicitud de seguimiento |

### 2.2) Pendiente
- Autenticacion de usuarios: se puede utilizar el modulo de autenticacion de django como podemos ver en este [enlace](https://docs.djangoproject.com/en/3.1/topics/auth/default/)
- Busqueda de usuarios: se puede utilizar las vistas por defecto de consulta dentro de django.
- Lista de ideas: por el momento se pueden ver todas las ideas del usuario "autenticado"
- Notificaciones: No puede encontré nada de notificaciones push en general. 
