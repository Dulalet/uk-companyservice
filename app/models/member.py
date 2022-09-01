from sqlalchemy import Column, Integer

from fastapi_utils.guid_type import GUID
from app.db.base_class import Base


class Member(Base):
    id = Column(Integer, primary_key=True, index=True)
    # user_id = Column(uuid_pkg, unique=True, index=True, nullable=False)
    user_uuid = Column(GUID, unique=True, index=True, nullable=False)
