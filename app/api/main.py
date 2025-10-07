from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from app.api.database import Base, engine
from app.api.routers import users, places, preferences, recommendations, schedules

app = FastAPI(
    title="Turistei API",
    description="API para cadastro de usuários e lugares turísticos",
    version="1.0.0"
)

app.mount("/src/img", StaticFiles(directory="app/api/src/img"), name="static_images")

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
