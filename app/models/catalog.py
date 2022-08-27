from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, Float
from sqlalchemy.orm import relationship
from app.core.config import PIECE

from app.db.base_class import Base


class Catalog(Base):
    id = Column(Integer, primary_key=True, index=True)
    department_id = Column(Integer, ForeignKey(
        "department.id"), nullable=False)
    code = Column(String(100), nullable=True)
    code_hatch = Column(String(100), nullable=True)
    name_ru = Column(String(1000))
    name_kz = Column(String(1000))
    pay_nds = Column(Boolean, default=False)
    price = Column(Float, default=0)
    quantity_type = Column(Integer, default=PIECE)

    department = relationship("Department", backref="catalog")
