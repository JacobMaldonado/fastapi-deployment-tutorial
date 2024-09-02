from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

class Usuario(BaseModel):
    nombre: str
    apellido: str
    edad: int

app = FastAPI()

usuario = Usuario(nombre="Juan", apellido="Perez", edad=30)

@app.get("/")
def read_root():
    """## Devuelve un saludo"""
    return "Hola Mundo"

@app.get("/objeto/{objeto_id}")
def leer_objeto(objeto_id: int, q: Optional[str] = None):
    """## Devuelve un objeto"""

    return {"objeto_id": objeto_id, "q": q}

@app.get("/usuario", response_model=Usuario)
def leer_usuario():
    """## Devuelve un usuario"""
    return usuario

@app.post("/usuario", response_model=Usuario)
def crear_usuario(nuevo_usuario: Usuario):
    """## Crea un usuario"""
    global usuario
    usuario = nuevo_usuario
    return usuario