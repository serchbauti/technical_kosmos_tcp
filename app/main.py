from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

app = FastAPI()
templates = Jinja2Templates(directory="templates")

message_history = []

@app.get("/", response_class=HTMLResponse)
async def serve_html(request: Request):
    """Handles GET requests to the root URL and serves the
    'index.html' template.
    Args:
        request (Request): The incoming HTTP request object.
    Returns:
        TemplateResponse: Renders the 'index.html' template with
        initial context including an empty response, message, and
        the message history.
    """
    return templates.TemplateResponse("index.html", {
        "request": request,
        "response": None,
        "message": None,
        "message_history": message_history
    })

@app.post("/message", response_class=HTMLResponse)
async def receipt_message(request: Request, message: str = Form(...)):
    """Handles POST requests to the '/message' endpoint, processes the
    user message, and updates the message history.
    Args:
        request (Request): The incoming HTTP request object.
        message (str): The user message submitted via form data.
    Returns:
        TemplateResponse: Renders the 'index.html' template with the
        processed response, original message, and updated message history.
    """
    print(f"Mensaje recibido: {message}")
    if message in ["DESCONEXION", "desconexion"]:
        response = "Desconectado"
        print(f"Cliente desconectado: {message}")
    else:
        response = message.upper()
        print(f"Respuesta al cliente: {response}")
    message_history.append({"user": message, "response": response})
    return templates.TemplateResponse("index.html", {
        "request": request,
        "response": response,
        "message": message,
        "message_history": message_history
    })

if __name__ == "__main__":
    import uvicorn
    print("Servidor iniciado...")
    print("Escuchando en el puerto 5000...")
    uvicorn.run(app, host="0.0.0.0", port=5000)