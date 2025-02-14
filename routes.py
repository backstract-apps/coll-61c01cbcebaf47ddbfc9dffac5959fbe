from fastapi import APIRouter, Request, Depends, HTTPException, UploadFile, Form
from sqlalchemy.orm import Session
from typing import List
import service, models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get('/parking_user/')
async def get_parking_user(db: Session = Depends(get_db)):
    try:
        return await service.get_parking_user(db)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/parking_user/id')
async def get_parking_user_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_parking_user_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/parking_user/')
async def post_parking_user(raw_data: schemas.PostParkingUser, db: Session = Depends(get_db)):
    try:
        return await service.post_parking_user(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/parking_user/id/')
async def put_parking_user_id(raw_data: schemas.PutParkingUserId, db: Session = Depends(get_db)):
    try:
        return await service.put_parking_user_id(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/parking_user/id')
async def delete_parking_user_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_parking_user_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

