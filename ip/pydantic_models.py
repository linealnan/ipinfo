from pydantic import BaseModel

from models import IpLocation, IpType

class IpInfo(BaseModel):
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