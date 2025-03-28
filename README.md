# Prueba Tecnica Kosmos TCP

Esta es una aplicación sencilla que simula un servidor TCP en FastAPI, se presenta una página HTML y procesa mensajes de usuario. La aplicación consta de dos endpoints principales: uno para servir la página HTML y otro para procesar mensajes enviados a través de un formulario.

## Características

- **GET /**: Sirve la plantilla `index.html`, que incluye un formulario para enviar mensajes.
- **POST /message**: Procesa el mensaje enviado, lo convierte a mayúsculas a menos que sea "DESCONEXION", y actualiza el historial de mensajes.

## Requisitos

- Python 3.7+
- FastAPI
- Jinja2
- Uvicorn

## Instalación

1. Clona el repositorio:

   ```bash
   git clone https://github.com/serchbauti/technical_kosmos_tcp
   cd app
   ```

2. Instala los paquetes requeridos:

   ```bash
   pip install -r requirements.txt
   ```

## Ejecución de la Aplicación

1. Inicia el servidor FastAPI usando Uvicorn:

   ```bash
   uvicorn app.main:app --reload
   ```

2. Abre tu navegador web y navega a `http://127.0.0.1:8000` para acceder a la aplicación.

## Uso

- Ingresa un mensaje en el campo de entrada y haz clic en "Enviar" para enviarlo.
- El servidor responderá mostrando el mensaje en mayúsculas, a menos que el mensaje sea "DESCONEXION", en cuyo caso responderá con "Desconectado".
- El historial de mensajes se muestra debajo del formulario, mostrando tanto el mensaje del usuario como la respuesta del servidor.

## Estructura de Archivos

- `app/main.py`: Contiene el código de la aplicación FastAPI.
- `templates/index.html`: La plantilla HTML para la aplicación.
- `requirements.txt`: Lista las dependencias necesarias para ejecutar la aplicación.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT.