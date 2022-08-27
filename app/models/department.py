from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class Department(Base):
    id = Column(Integer, primary_key=True, index=True)
    company_id = Column(Integer, ForeignKey("company.id"), nullable=False)
    name_ru = Column(String(1000))
    name_kz = Column(String(1000))
    code = Column(String(100))

    company = relationship("Company", backref="departments")
