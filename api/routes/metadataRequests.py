from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database.connection import get_db
from database.models import MetadataRequests
from schemas.metadataModels import MetadataRequest, MetadataResponse
from uuid import UUID
from typing import List

from controller.metadataRequestController import create, fetchById, fetchAll

router = APIRouter(tags=["metadatas"])


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=MetadataResponse)
async def create_request(metaReq: MetadataRequest, db: Session = Depends(get_db)):
    return create(db=db, metaReq=metaReq)


@router.get("/all", status_code=status.HTTP_200_OK, response_model=List[MetadataResponse])
async def get_all_requests(db: Session = Depends(get_db)):
    return fetchAll(db=db)


@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=MetadataResponse)
async def get_request(id, db: Session = Depends(get_db)):
    try:
        return fetchById(db=db, id=id)
    except:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Meatadata Request not found"
        )
