from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional ##para dizer que o campo pode ser opcional definindo nome: Optional[str]

app = FastAPI()