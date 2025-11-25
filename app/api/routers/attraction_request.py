from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.api.database import get_db
from app.api.models.attraction_request import AttractionRequest
from app.api.models.place import Place
from app.api.schemas.attraction_request import AttractionRequestCreate, AttractionRequestOut
from app.api.schemas.place import PlaceCreate
from app.api.services.place_service import create_place

router = APIRouter(
    prefix="/attractions",
    tags=["attractions"]
)

# ------------------------------
# 1. Usuário solicita atração
# ------------------------------
@router.post("/request", response_model=AttractionRequestOut)
def request_attraction(data: AttractionRequestCreate, db: Session = Depends(get_db)):
    req = AttractionRequest(**data.dict())
    db.add(req)
    db.commit()
    db.refresh(req)
    return req

# ------------------------------
# 2. Admin lista solicitações pendentes
# ------------------------------
@router.get("/admin/requests", response_model=list[AttractionRequestOut])
def get_pending_requests(db: Session = Depends(get_db)):
    return db.query(AttractionRequest).filter(
        AttractionRequest.status == "pendente"
    ).all()

# ------------------------------
# 3. Admin aprova → cria Place
# ------------------------------
@router.post("/admin/requests/{request_id}/approve")
def approve_request(request_id: int, db: Session = Depends(get_db)):
    req = db.query(AttractionRequest).get(request_id)

    if not req:
        raise HTTPException(status_code=404, detail="Solicitação não encontrada")

    req.status = "aprovado"

    # Criar Place completo, incluindo preferences vazias
    place_data = PlaceCreate(
        name=req.name,
        city=req.city,
        description=req.description,
        latitude=req.latitude,
        longitude=req.longitude,
        image_url=None,
        preferences=[]  # usuário comum não define isso
    )

    new_place = create_place(db, place_data)

    db.commit()

    return {"msg": "Atração aprovada e cadastrada", "place_id": new_place.id}

# ------------------------------
# 4. Admin rejeita
# ------------------------------
@router.post("/admin/requests/{request_id}/reject")
def reject_request(request_id: int, db: Session = Depends(get_db)):
    req = db.query(AttractionRequest).get(request_id)

    if not req:
        raise HTTPException(status_code=404, detail="Solicitação não encontrada")

    req.status = "rejeitado"
    db.commit()

    return {"msg": "Solicitação rejeitada"}
