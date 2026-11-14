# Blog Django - Pre-entrega 8

Proyecto de un blog web desarrollado con Django. En esta entrega, la base
creada en la pre-entrega 7 se transforma en un sitio navegable con páginas
HTML, templates reutilizables y estilos CSS personalizados.

## Novedades de esta entrega

- Se agregaron vistas basadas en funciones que renderizan templates HTML.
- Se creó un layout base reutilizable en `posts/templates/posts/base.html`.
- Se implementó herencia de templates para evitar repetir la estructura del
  sitio.
- Se incorporó un menú de navegación entre las páginas principales.
- Se agregaron las páginas:
  - Inicio.
  - Posts.
  - Acerca de.
- Se incorporaron archivos estáticos con una hoja de estilos CSS.
- Se aplicaron estilos visuales al encabezado, menú, contenido, títulos,
  párrafos y pie de página.

Esta entrega todavía no utiliza modelos, formularios ni persistencia de datos.
El objetivo es practicar el flujo:

```text
Ruta -> Vista -> Template -> Archivo estático
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
    ├── views.py
    ├── urls.py
    ├── models.py
    ├── admin.py
    ├── tests.py
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
            └── css/
                └── style.css
```

## Rutas disponibles

| Ruta | Página |
| --- | --- |
| `/` | Página de inicio |
| `/posts/` | Listado de posts |
| `/acerca/` | Información sobre el autor y el sitio |
| `/admin/` | Panel de administración de Django |

## Instalación y ejecución

### 1. Clonar el repositorio

```bash
git clone https://github.com/gcostaclases/ch-pre-entrega-8.git
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

### 5. Ejecutar el servidor

```bash
python manage.py runserver
```

Luego, abrir [http://127.0.0.1:8000/](http://127.0.0.1:8000/) en el navegador.

## Aplicación principal

- `posts`: aplicación encargada de las páginas, vistas, templates y archivos
  estáticos del blog.
