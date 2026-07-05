from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, schemas
from app.database import get_db

router = APIRouter(prefix="/api/destinations", tags=["destinations"])


@router.get("/", response_model=list[schemas.Destination])
def list_destinations(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_destinations(db, skip=skip, limit=limit)


@router.get("/{destination_id}", response_model=schemas.Destination)
def get_destination(destination_id: int, db: Session = Depends(get_db)):
    dest = crud.get_destination(db, destination_id)
    if not dest:
        raise HTTPException(status_code=404, detail="Destination not found")
    return dest


@router.post("/", response_model=schemas.Destination, status_code=201)
def create_destination(destination: schemas.DestinationCreate, db: Session = Depends(get_db)):
    return crud.create_destination(db, destination)


@router.put("/{destination_id}", response_model=schemas.Destination)
def update_destination(destination_id: int, destination: schemas.DestinationUpdate, db: Session = Depends(get_db)):
    dest = crud.update_destination(db, destination_id, destination)
    if not dest:
        raise HTTPException(status_code=404, detail="Destination not found")
    return dest


@router.delete("/{destination_id}", status_code=204)
def delete_destination(destination_id: int, db: Session = Depends(get_db)):
    dest = crud.delete_destination(db, destination_id)
    if not dest:
        raise HTTPException(status_code=404, detail="Destination not found")
