from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database.connection import get_db
from database.models import MetadataRequests
from schemas.metadataModels import MetadataRequest, MetadataResponse
from uuid import UUID

from controller.metadataRequestController import create_meta_request, get_meta_req_by_id

router = APIRouter(tags=["metadatas"])

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=MetadataResponse)
async def create_request(metaReq: MetadataRequest, db: Session = Depends(get_db)):
    return create_meta_request(db=db, metaReq=metaReq)

@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=MetadataResponse)
async def get_request(id, db: Session = Depends(get_db)):
    return get_meta_req_by_id(db=db, id=id)
