from app.api.database import SessionLocal
from app.api.models.user import Preference

db = SessionLocal()

preferencias_fixas = [
    "bares", "shows", "restaurantes", "pontos turísticos", "praia"
]

for nome in preferencias_fixas:
    if not db.query(Preference).filter_by(name=nome).first():
        db.add(Preference(name=nome))

db.commit()
db.close()
