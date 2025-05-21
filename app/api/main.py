from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.database import Base, engine
from app.api.routers import users, places  

# Cria as tabelas no banco de dados
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Turistei API",
    description="API para cadastro de usuários e lugares turísticos",
    version="1.0.0"
)

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

@app.get("/")
def root():
    return {"message": "Bem-vindo à Turistei API!"}
