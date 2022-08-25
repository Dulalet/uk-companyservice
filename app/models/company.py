from enum import Enum
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship

from app.db.base_class import Base

class TaxModesEnum(Enum):
    tax_farm_mode = (1, 'Налоговый режим для крестьянских и фермерских хозяйств')
    tax_low_too_mode = (2, 'Налоговый режим для малых предприятий на основе патента')
    tax_general_mode = (3, 'Общеустановленная система налогообложения')
    tax_simplified_mode = (4, 'Упрощенная система налогообложения')


class Company(Base):
    id = Column(Integer, primary_key=True, index=True)
    bin_iin = Column(String(12), index=True, unique=True)
    name = Column(String(1000), nullable=True)
    address = Column(String(1000), nullable=True)
    tax_mode = Column(Integer, Enum(TaxModesEnum))
    