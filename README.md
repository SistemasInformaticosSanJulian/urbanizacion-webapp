# Proyecto de Gestión de Urbanización

Este es un proyecto desarrollado con **Django 5.2**. A continuación, se detallan las instrucciones para su descarga, configuración y ejecución en un entorno local.

## 1. Descarga del Proyecto

Para descargar este proyecto como un archivo ZIP:

1. Dirígete a la página principal del repositorio en la plataforma (GitHub, GitLab, etc.).
2. Haz clic en el botón verde **"Code"** o **"Descargar"**.
3. Selecciona la opción **"Download ZIP"**.
4. Descomprime el archivo en la ubicación de tu preferencia.

## 2. Requisitos Previos

Asegúrate de tener instalados los siguientes componentes:
*   Python 3.10 o superior.
*   Pip (Administrador de paquetes de Python).

## 3. Configuración del Entorno Virtual

Es recomendable utilizar un entorno virtual para aislar las dependencias del proyecto.

### En Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

### En Linux / macOS:
```bash
python3 -m venv venv
source venv/bin/activate
```

## 4. Instalación de Dependencias

Una vez activado el entorno virtual, instala Django y las librerías necesarias.

Si cuentas con un archivo `requirements.txt`:
```bash
pip install -r requirements.txt
```

*(Nota: Si agregas más librerías, recuerda guardarlas con `pip freeze > requirements.txt`)*

## 5. Ejecución del Servidor

Para iniciar el servidor de desarrollo, utiliza el siguiente comando:

```bash
python manage.py runserver
```

Una vez iniciado, podrás acceder al proyecto en tu navegador mediante la dirección:
[http://127.0.0.1:8000/](http://127.0.0.1:8000/)

*   **Usuario:** `admin`
*   **Contraseña:** `admin`

## Estructura del Proyecto
*   `urbanizacion/`: Configuración principal del proyecto (settings, urls).
*   `venta/`: Aplicación encargada de la gestión de ventas.
*   `docs/`: Documentación técnica y diagramas de base de datos.
*   `static/`: Archivos estáticos (CSS, JS, imágenes).
