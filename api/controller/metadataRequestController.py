from uuid import UUID

from database.models import MetadataRequests
from schemas.metadataModels import MetadataRequest
from sqlalchemy.orm import Session

def create_meta_request(db: Session, metaReq:MetadataRequest):
    metaRequest = MetadataRequests(client_name=metaReq.client_name, file_name=metaReq.file_name, file_content=metaReq.file_content)
    db.add(metaRequest)
    db.commit()
    db.refresh(metaRequest)
    return metaRequest

def get_meta_req_by_id(db: Session, id: UUID):
    return db.query(MetadataRequests).filter_by(id=id).one()