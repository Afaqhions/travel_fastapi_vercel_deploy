from sqlalchemy.orm import Session
from app import models, schemas


def get_destinations(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Destination).offset(skip).limit(limit).all()


def get_destination(db: Session, destination_id: int):
    return db.query(models.Destination).filter(models.Destination.id == destination_id).first()


def create_destination(db: Session, destination: schemas.DestinationCreate):
    db_dest = models.Destination(**destination.model_dump())
    db.add(db_dest)
    db.commit()
    db.refresh(db_dest)
    return db_dest


def update_destination(db: Session, destination_id: int, destination: schemas.DestinationUpdate):
    db_dest = get_destination(db, destination_id)
    if not db_dest:
        return None
    for key, value in destination.model_dump(exclude_unset=True).items():
        setattr(db_dest, key, value)
    db.commit()
    db.refresh(db_dest)
    return db_dest


def delete_destination(db: Session, destination_id: int):
    db_dest = get_destination(db, destination_id)
    if not db_dest:
        return None
    db.delete(db_dest)
    db.commit()
    return db_dest
