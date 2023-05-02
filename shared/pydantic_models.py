from pydantic import BaseModel
import enum

class IpType(enum.Enum):
    """ Тип ip адреса """
    SOME_TYPE='SOME_TYPE'

class IpLanguages(BaseModel):
    code: str
    name: str
    native: str

class IpLocation(BaseModel):
    geoname_id: int
    capital: str
    languages: IpLanguages
