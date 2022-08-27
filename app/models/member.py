from sqlalchemy import Column, Integer

from app.db.base_class import Base


class Member(Base):
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, unique=True, index=True, nullable=False)
