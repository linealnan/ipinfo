from sqlalchemy import Boolean, Column, Float, Integer, String
from sqlalchemy.orm import relationship, mapped_column
from sqlalchemy import Enum

from models import IpLocation, IpType

from .database import Base

IpTypeEnum: Enum = Enum(
    IpType,
    name="ip_type",
    create_constraint=True,
    #metadata=Base.metadata,
    validate_strings=True,
)
