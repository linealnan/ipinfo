from pydantic import BaseModel, BaseSettings 

class IpInfo(BaseModel):
    ip: str