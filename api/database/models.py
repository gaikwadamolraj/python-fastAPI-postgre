import uuid
from datetime import datetime

from sqlalchemy import Column, String, DateTime
from sqlalchemy.dialects.postgresql import UUID
from database.connection import Base, engine


class MetadataRequests(Base):
    __tablename__ = "metadatarequests"

    id = Column(UUID(as_uuid=True), primary_key=True,
                default=uuid.uuid4, index=True)
    client_name = Column(String)
    file_name = Column(String)
    file_content = Column(String)
    response_metadata = Column(String)
    created_by = Column(String)
    updated_by = Column(String)
    created_on = Column(DateTime, default=datetime.utcnow)
    updated_on = Column(DateTime, default=datetime.utcnow)


Base.metadata.create_all(engine)
