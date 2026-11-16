# Blog Django - Pre-entrega 10

Proyecto de un blog web desarrollado con Django. Esta entrega continúa el
trabajo de la pre-entrega 9 y agrega un CRUD completo de publicaciones desde
la interfaz del sitio, junto con la carga y visualización de imágenes.

## Novedades respecto de la pre-entrega 9

- Se agregó el campo opcional `imagen` al modelo `Post`, configurado con
  `upload_to="posts/"`.
- Se agregó el campo `slug` para identificar cada publicación mediante una URL
  amigable y única.
- Se creó `posts/forms.py` con `PostForm`, un `ModelForm` para crear y editar
  publicaciones.
- Se incorporó validación para exigir títulos de al menos cinco caracteres.
- Se implementaron las operaciones CRUD desde el sitio:
  - Crear publicaciones.
  - Listar publicaciones publicadas.
  - Ver el detalle de una publicación.
  - Editar publicaciones existentes.
  - Eliminar publicaciones con confirmación previa.
- Los formularios de creación y edición procesan datos y archivos mediante
  `request.POST` y `request.FILES`.
- Se agregó soporte para imágenes mediante `MEDIA_URL` y `MEDIA_ROOT`.
- Se configuró el proyecto para servir archivos media durante el desarrollo.
- Se agregaron templates para el detalle, el formulario y la confirmación de
  eliminación.
- El listado y el detalle muestran la imagen cargada o una imagen por defecto
  cuando el post no tiene imagen.
- Se agregó la migración `0002_post_imagen_post_slug.py`.
- Se incorporó Pillow en `requirements.txt` para poder utilizar
  `ImageField`.

La entrega mantiene las funcionalidades de la pre-entrega 9: modelo `Post`
con estados, persistencia en SQLite, listado mediante el ORM, administración
desde `/admin/`, navegación, páginas de inicio y acerca de, herencia de
templates y estilos CSS.

El flujo principal para el CRUD es:

```text
Ruta -> Vista -> ModelForm/ORM -> Base de datos y media -> Template
```

## Tecnologías utilizadas

- Python
- Django 6.1.3
- Pillow 13.0.0
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
├── media/
│   └── posts/
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
    ├── forms.py
    ├── models.py
    ├── tests.py
    ├── urls.py
    ├── views.py
    ├── migrations/
    │   ├── 0001_initial.py
    │   ├── 0002_post_imagen_post_slug.py
    │   └── __init__.py
    │
    ├── templates/
    │   └── posts/
    │       ├── base.html
    │       ├── inicio.html
    │       ├── lista_posts.html
    │       ├── detalle_post.html
    │       ├── post_form.html
    │       ├── post_confirm_delete.html
    │       └── acerca.html
    │
    └── static/
        └── posts/
            ├── css/
            │   └── estilos.css
            └── img/
                ├── default.png
                └── logo-glups.png
```

## Rutas disponibles

| Ruta | Página |
| --- | --- |
| `/` | Página de inicio |
| `/posts/` | Listado de posts publicados |
| `/posts/crear/` | Formulario para crear un post |
| `/post/<slug>/` | Detalle de un post |
| `/post/<slug>/editar/` | Formulario para editar un post |
| `/post/<slug>/eliminar/` | Confirmación para eliminar un post |
| `/acerca/` | Información sobre el autor y el sitio |
| `/admin/` | Panel de administración de Django |

## Manejo de imágenes

El modelo utiliza:

```python
imagen = models.ImageField(
    upload_to="posts/",
    null=True,
    blank=True,
)
```

Las imágenes subidas se guardan en `media/posts/`. En `settings.py` se
configuraron:

```python
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"
```

Además, `blog_project/urls.py` agrega las rutas para servir esos archivos
cuando `DEBUG` está habilitado. El formulario utiliza
`enctype="multipart/form-data"` y las vistas reciben `request.FILES` para que
la carga funcione correctamente.

## Instalación y ejecución

### 1. Crear el entorno virtual

Windows:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

macOS o Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 2. Instalar las dependencias

```bash
pip install -r requirements.txt
```

Pillow se instala junto con el resto de las dependencias y es necesario para
trabajar con `ImageField`.

### 3. Aplicar las migraciones

```bash
python manage.py migrate
```

### 4. Crear un superusuario (opcional)

El panel de administración continúa disponible para gestionar publicaciones:

```bash
python manage.py createsuperuser
```

### 5. Ejecutar el servidor

```bash
python manage.py runserver
```

Luego, abrir [http://127.0.0.1:8000/](http://127.0.0.1:8000/) en el navegador.

## Cómo probar el CRUD y la carga de imágenes

1. Ingresar en `/posts/crear/`.
2. Completar título, contenido, autor y estado.
3. Seleccionar una imagen opcional y guardar el post.
4. Verificar la imagen en el listado y en el detalle del post.
5. Entrar en `/post/<slug>/editar/` para modificar los datos o cambiar la
   imagen.
6. Entrar en `/post/<slug>/eliminar/` y confirmar la eliminación.
7. Crear también un post sin imagen para comprobar que se muestra la imagen
   predeterminada sin romper el template.

El listado muestra únicamente posts cuyo estado es `Publicado`. Los posts
pueden seguir administrándose desde
[http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/).

## Aplicación principal

- `posts`: aplicación encargada del modelo, migraciones, formulario,
  administración, vistas CRUD, templates y archivos estáticos del blog.
