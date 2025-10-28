from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from app.api.database import Base, engine
from app.api.routers import users, places, preferences, recommendations, schedules
import os

app = FastAPI(
    title="Turistei API",
    description="API para cadastro de usuários e lugares turísticos",
    version="1.0.0"
)

# Caminho absoluto, garantindo compatibilidade
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMG_DIR = os.path.join(BASE_DIR, ".\src\img")

app.mount("/static", StaticFiles(directory=IMG_DIR), name="static")

# Configurações de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # ou especifique origens seguras
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Rotas principais
app.include_router(users.router)
app.include_router(places.router)
app.include_router(preferences.router)
app.include_router(recommendations.router)
app.include_router(schedules.router)

@app.get("/")
def root():
    return {"message": "Bem-vindo à Turistei API!"}

# Cria as tabelas no banco de dados
Base.metadata.create_all(bind=engine)
