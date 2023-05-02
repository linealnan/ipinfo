from sqlalchemy import Boolean, Column, Float, Integer, String
from sqlalchemy.orm import relationship, mapped_column
from sqlalchemy import Enum

from models import IpLocation, IpType, IpTypeEnum

from database import Base

class IpInfo(Base):
    __tablename__ = "ip_info"

    id = mapped_column(Integer, primary_key=True, index=True)
    ip = Column(String, unique=True)
    type = Column('ip_type_enum', IpTypeEnum, nullable=False)
    continent_code = Column(String, nullable=False)
    continent_name = Column(String, nullable=False)
    country_code = Column(String, nullable=False)
    country_name = Column(String, nullable=False)
    region_code = Column(String, nullable=False)
    region_name = Column(String, nullable=False)
    city = Column(String, nullable=False)
    zip = Column(String, nullable=False)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    #location = IpLocation @TODO REFERENCE
    country_flag = Column(String, nullable=False)
    country_flag_emoji = Column(String, nullable=False)
    country_flag_emoji_unicode = Column(String, nullable=False)
    calling_code = Column(Integer, nullable=False)
    is_eu = Column(Boolean, nullable=False)
    