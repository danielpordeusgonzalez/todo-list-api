from fastapi import FastAPI
from pydantic import BaseModel
# from typing import Optional ##para dizer que o campo pode ser opcional definindo nome: Optional[str]
from datetime import date

app = FastAPI()

class Mensagem(BaseModel):
    mensagem: str
    realizada: bool
    
listMensagem = []

@app.post("/mensagem")
def mensagem(mensagem: Mensagem):
    try:
        listMensagem.append(mensagem)
        return {"status": "sucesso"}
    except:
        return {"status": "erro"}
    

@app.get("/verMensagem")
def verMensagem(opcao: int = 0):
    if opcao == 0:
        return listMensagem
    elif opcao == 1:
        return list(filter(lambda x: x.realizada == False, listMensagem))
    elif opcao == 2:
        return list(filter(lambda x: x.realizada == True, listMensagem))
    
@app.get("/verMensagem/{id}")
def listar(id: int):
    try:
        return listMensagem[id]
    except:
        return {"status": "erro"}
    
@app.post("/editarMensagem")
def editar(id: int):
    try:
        listMensagem[id].realizada = not listMensagem[id].realizada
        return {"status": "sucesso"}
    except:
        return {"status": "erro"}

@app.post("/deletarMensagem")
def deletar(id: int):
    try:
        del listMensagem[id]
        return {"status": "sucesso"}
    except:
        return {"status": "erro"}