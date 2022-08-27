from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean
from sqlalchemy.orm import relationship, backref
from sqlalchemy.dialects.postgresql import ENUM
from sqlalchemy.sql import func

from app.db.base_class import Base
from app.models.enums import NDSTypesEnum, TaxModesEnum, MemberTypesEnum


class Company(Base):
    id = Column(Integer, primary_key=True, index=True)
    bin_iin = Column(String(12), index=True, unique=True)
    name = Column(String(1000), nullable=True)
    address = Column(String(1000), nullable=True)
    tax_mode = Column(ENUM(TaxModesEnum), default=3)
    pay_nds = Column(Boolean, default=False)
    seria_nds = Column(String(100), nullable=True)
    number_nds = Column(String(100), nullable=True)
    nds_type = Column(ENUM(NDSTypesEnum), default=0)
    pin_prog = Column(String(100), nullable=True)
    pin_kassa_in = Column(String(100), nullable=True)
    pin_close_shift = Column(String(100), nullable=True)
    pin_rmni = Column(String(100), nullable=True)
    filled_fields = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())


class CompanyMember(Base):
    __tablename__ = 'company_members'
    company_id = Column(ForeignKey('company.id'), primary_key=True)
    member_id = Column(ForeignKey('member.id'), primary_key=True)
    type = Column(ENUM(MemberTypesEnum), default=1)

    company = relationship("Company", backref=backref(
        "members", cascade="save-update, merge, delete, delete-orphan"))
    member = relationship("Member", backref=backref(
        "companies", cascade="save-update, merge, delete, delete-orphan"))
