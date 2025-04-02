# app/main.py
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from app.runner import run_code

app = FastAPI()
templates = Jinja2Templates(directory="templates")

language_options = [
    {"value": "python", "label": "Python"},
    {"value": "javascript", "label": "JavaScript"},
]


@app.get("/run", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", 
                                      {"request": request, 
                                       "result": "", 
                                       "language_options":language_options, 
                                       "code": ""})

@app.post("/run", response_class=HTMLResponse)
async def execute_code(request: Request, code: str = Form(...), language: str = Form(...)):
    
    code = code.strip()
    
    result = run_code(language, code)

    return templates.TemplateResponse("index.html", 
                                      {"request": request, 
                                       "result": result, 
                                       "code": code, 
                                       "language_options":language_options, 
                                       "language": language})

@app.get("/terminal", response_class=HTMLResponse)
async def terminal_view(request: Request):
    return templates.TemplateResponse("terminal.html", {"request": request})
