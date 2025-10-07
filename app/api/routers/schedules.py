# app/api/routes/schedule.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.api.database import get_db
from app.api.models.schedule import Schedule, ScheduleItem
from app.api.schemas.schedule import ScheduleCreate, ScheduleOut
from pydantic import BaseModel
from sqlalchemy.orm import Session, joinedload

router = APIRouter(
    prefix="/schedules",
    tags=["schedules"]
)

class SetPlaceRequest(BaseModel):
    place_id: int

@router.post("/", response_model=ScheduleOut)
def create_schedule(schedule_data: ScheduleCreate, db: Session = Depends(get_db)):
    new_schedule = Schedule(
        title=schedule_data.title,
        user_id=schedule_data.user_id,
        date=schedule_data.date
    )
    db.add(new_schedule)
    db.flush()

    for item in schedule_data.items:
        new_item = ScheduleItem(
            schedule_id=new_schedule.id,
            place_id=item.place_id,
            custom_name=item.title,       # 🔹 mapeia title -> custom_name
            start_time=item.start_time,
            end_time=item.end_time,
        )
        db.add(new_item)

    db.commit()
    db.refresh(new_schedule)

    # 🔹 Transformar manualmente o response
    return {
        "id": new_schedule.id,
        "title": new_schedule.title,
        "date": new_schedule.date.isoformat() if new_schedule.date else None,
        "user_id": new_schedule.user_id,
        "items": [
            {
                "id": i.id,
                "title": i.custom_name,   # 🔹 mapeia de volta
                "description": "",        # 🔹 placeholder (não existe no banco)
                "start_time": i.start_time,
                "end_time": i.end_time,
                "place_id": i.place_id
            }
            for i in new_schedule.items
        ]
    }

# 🟢 Listar todos os roteiros de um usuário
@router.get("/user/{user_id}", response_model=list[ScheduleOut])
def list_user_schedules(user_id: int, db: Session = Depends(get_db)):
    schedules = (
        db.query(Schedule)
        .options(
            joinedload(Schedule.items).joinedload(ScheduleItem.place)  # carrega atividades + locais
        )
        .filter(Schedule.user_id == user_id)
        .order_by(Schedule.date.asc())
        .all()
    )

    if not schedules:
        raise HTTPException(status_code=404, detail="Nenhum roteiro encontrado para este usuário")

    return schedules

# 🗑️ Deletar um roteiro específico
@router.delete("/{schedule_id}", response_model=dict)
def delete_schedule(schedule_id: int, db: Session = Depends(get_db)):
    schedule = db.query(Schedule).filter(Schedule.id == schedule_id).first()
    if not schedule:
        raise HTTPException(status_code=404, detail="Roteiro não encontrado")

    db.delete(schedule)
    db.commit()

    return {"message": f"Roteiro {schedule_id} deletado com sucesso"}


# 🗑️ Deletar todos os roteiros de um usuário
@router.delete("/user/{user_id}", response_model=dict)
def delete_all_schedules_for_user(user_id: int, db: Session = Depends(get_db)):
    schedules = db.query(Schedule).filter(Schedule.user_id == user_id).all()
    if not schedules:
        raise HTTPException(status_code=404, detail="Nenhum roteiro encontrado para este usuário")

    for schedule in schedules:
        db.delete(schedule)

    db.commit()

    return {"message": f"Todos os roteiros do usuário {user_id} foram deletados com sucesso"}