# Blog Django

Proyecto de un blog web desarrollado con Django. La aplicación principal
`posts` está preparada para manejar las publicaciones del blog.

## Instalación y ejecución

### 1. Clonar el repositorio

```bash
git clone https://github.com/gcostaclases/ch-pre-entrega-7.git
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

### 5. Levantar el servidor de desarrollo

```bash
python manage.py runserver
```

Abrí [http://127.0.0.1:8000/](http://127.0.0.1:8000/) en el navegador.

## Aplicación principal

- `posts`: aplicación encargada de las publicaciones del blog.
