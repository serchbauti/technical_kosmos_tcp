from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

app = FastAPI()
templates = Jinja2Templates(directory="templates")

message_history = []

@app.get("/", response_class=HTMLResponse)
async def serve_html(request: Request):
    return templates.TemplateResponse("index.html", {
        "request": request,
        "response": None,
        "message": None,
        "message_history": message_history
    })

@app.post("/message", response_class=HTMLResponse)
async def receipt_message(request: Request, message: str = Form(...)):
    if message in ["DESCONEXION", "desconexion"]:
        response = "Desconectado"
    else:
        response = message.upper()
    message_history.append({"user": message, "response": response})
    return templates.TemplateResponse("index.html", {
        "request": request,
        "response": response,
        "message": message,
        "message_history": message_history
    })