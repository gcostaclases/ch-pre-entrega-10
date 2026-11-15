# Blog Django - Pre-entrega 9

Proyecto de un blog web desarrollado con Django. Esta entrega continúa el
trabajo de la pre-entrega 8 y conecta el sitio con una base de datos SQLite
mediante el ORM de Django.

## Novedades respecto de la pre-entrega 8

- Se creó el modelo `Post` en `posts/models.py`.
- Se agregaron los campos:
  - `titulo`.
  - `contenido`.
  - `autor`.
  - `fecha_creacion`, completado automáticamente con `auto_now_add=True`.
  - `estado`, con las opciones Borrador, Publicado y Archivado.
- Se implementó `__str__` para mostrar el título de cada publicación.
- Se configuró el orden predeterminado de los posts por fecha de creación
  descendente.
- Se generó y aplicó la migración inicial del modelo.
- Se registró `Post` en el panel de administración de Django.
- Se creó `PostAdmin` con:
  - Columnas de título, autor, fecha de creación y estado.
  - Búsqueda por título, contenido y autor.
  - Filtros por estado y fecha de creación.
  - Edición directa del estado desde el listado.
- Se incorporó el flujo de creación de un superusuario y carga de posts desde
  `/admin/`.
- La vista de listado dejó de utilizar contenido estático y consulta mediante
  el ORM únicamente los posts publicados, ordenados por fecha de creación.
- `lista_posts.html` muestra dinámicamente los posts con un bucle de Django
  Template Language e informa cuando no hay publicaciones.

La entrega mantiene las funcionalidades de la pre-entrega 8: rutas, vistas,
herencia de templates, menú de navegación, páginas de inicio, posts y acerca
de, además de los estilos CSS.

El flujo principal ahora es:

```text
Ruta -> Vista -> ORM -> Contexto -> Template -> Archivo estático
```

## Tecnologías utilizadas

- Python
- Django 6.1.3
- HTML5
- CSS3
- SQLite

## Estructura principal

```text
blog_django/
├── manage.py
├── README.md
├── requirements.txt
├── db.sqlite3
│
├── blog_project/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
└── posts/
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── tests.py
    ├── urls.py
    ├── views.py
    ├── migrations/
    │   ├── 0001_initial.py
    │   └── __init__.py
    │
    ├── templates/
    │   └── posts/
    │       ├── base.html
    │       ├── inicio.html
    │       ├── lista_posts.html
    │       └── acerca.html
    │
    └── static/
        └── posts/
            ├── css/
            │   └── estilos.css
            └── img/
                └── logo-glups.png
```

## Rutas disponibles

| Ruta | Página |
| --- | --- |
| `/` | Página de inicio |
| `/posts/` | Listado de posts publicados |
| `/acerca/` | Información sobre el autor y el sitio |
| `/admin/` | Panel de administración de Django |

## Instalación y ejecución

### 1. Clonar el repositorio

```bash
git clone https://github.com/gcostaclases/ch-pre-entrega-9.git
cd blog_django
```

### 2. Crear el entorno virtual

macOS o Linux:

```bash
python3 -m venv .venv
```

Windows:

```powershell
py -m venv .venv
```

### 3. Activar el entorno virtual

macOS o Linux:

```bash
source .venv/bin/activate
```

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 4. Instalar las dependencias

```bash
pip install -r requirements.txt
```

### 5. Aplicar las migraciones

```bash
python manage.py migrate
```

### 6. Crear un superusuario

```bash
python manage.py createsuperuser
```

Seguí las instrucciones de la terminal para definir el nombre de usuario,
email y contraseña.

### 7. Ejecutar el servidor

```bash
python manage.py runserver
```

Luego, abrir [http://127.0.0.1:8000/](http://127.0.0.1:8000/) en el navegador.

Para administrar las publicaciones, ingresar en
[http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/) con el
superusuario y crear al menos tres posts. La página `/posts/` mostrará solo
las publicaciones cuyo estado sea `Publicado`.

## Aplicación principal

- `posts`: aplicación encargada de los modelos, migraciones, administración,
  vistas, templates y archivos estáticos del blog.
