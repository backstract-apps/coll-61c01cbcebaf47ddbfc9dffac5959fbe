from sqlalchemy.orm import Session
from sqlalchemy import and_, or_
from typing import *
from fastapi import Request, UploadFile, HTTPException
import models, schemas
import boto3

import jwt

import datetime

from pathlib import Path

async def get_parking_user(db: Session):

    parking_user_all = db.query(models.ParkingUser).all()
    parking_user_all = [new_data.to_dict() for new_data in parking_user_all] if parking_user_all else parking_user_all

    res = {
        'parking_user_all': parking_user_all,
    }
    return res

async def get_parking_user_id(db: Session, id: int):

    parking_user_one = db.query(models.ParkingUser).filter(models.ParkingUser.id == id).first() 
    parking_user_one = parking_user_one.to_dict() if parking_user_one else parking_user_one

    res = {
        'parking_user_one': parking_user_one,
    }
    return res

async def post_parking_user(db: Session, raw_data: schemas.PostParkingUser):
    id:str = raw_data.id
    name:str = raw_data.name
    email:str = raw_data.email
    password:str = raw_data.password


    record_to_be_added = {'id': id, 'name': name, 'email': email, 'password': password}
    new_parking_user = models.ParkingUser(**record_to_be_added)
    db.add(new_parking_user)
    db.commit()
    db.refresh(new_parking_user)
    parking_user_inserted_record = new_parking_user.to_dict()

    res = {
        'parking_user_inserted_record': parking_user_inserted_record,
    }
    return res

async def put_parking_user_id(db: Session, raw_data: schemas.PutParkingUserId):
    id:str = raw_data.id
    name:str = raw_data.name
    email:str = raw_data.email
    password:str = raw_data.password


    parking_user_edited_record = db.query(models.ParkingUser).filter(models.ParkingUser.id == id).first()
    for key, value in {'id': id, 'name': name, 'email': email, 'password': password}.items():
          setattr(parking_user_edited_record, key, value)
    db.commit()
    db.refresh(parking_user_edited_record)
    parking_user_edited_record = parking_user_edited_record.to_dict() 

    res = {
        'parking_user_edited_record': parking_user_edited_record,
    }
    return res

async def delete_parking_user_id(db: Session, id: int):

    parking_user_deleted = None
    record_to_delete = db.query(models.ParkingUser).filter(models.ParkingUser.id == id).first()

    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        parking_user_deleted = record_to_delete.to_dict() 

    res = {
        'parking_user_deleted': parking_user_deleted,
    }
    return res

