import enum
from pydantic import BaseModel

class IpType(enum.Enum):
    SOME_TYPE='SOME_TYPE'

class IpLanguages(BaseModel):
    code: str
    name: str
    native: str

class IpLocation(BaseModel):
    geoname_id: int
    capital: str
    languages: IpLanguages

class IpstackComResponse(BaseModel):
   ip: str
   type: IpType
   continent_code: str
   continent_name: str
   country_code: str
   country_name: str
   region_code: str
   region_name: str
   city: str
   zip: str
   latitude: float
   longitude: float
   location: IpLocation
   country_flag: str
   country_flag_emoji: str
   country_flag_emoji_unicode: str
   calling_code: int
   is_eu: bool

class IpstackComResponseErrorData(BaseModel):
    code: int
    type: str
    info: str

class IpstackComResponseError(BaseModel):
    success: bool
    error: list[IpstackComResponseErrorData]

