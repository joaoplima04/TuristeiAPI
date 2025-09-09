from app.api.models.schedule import ScheduleItem


@router.post("/", response_model=ScheduleOut)
def create_schedule(schedule_data: ScheduleCreate, db: Session = Depends(get_db)):
    schedule = Schedule(title=schedule_data.title, user_id=schedule_data.user_id)

    db.add(schedule)
    db.commit()
    db.refresh(schedule)

    # criar itens
    for item in schedule_data.items:
        schedule_item = ScheduleItem(
            schedule_id=schedule.id,
            place_id=item.place_id,
            custom_name=item.custom_name,
            start_time=item.start_time,
            duration_minutes=item.duration_minutes
        )
        db.add(schedule_item)

    db.commit()
    db.refresh(schedule)
    return schedule
