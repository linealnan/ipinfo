from typing import Annotated
from fastapi import Depends
import requests
from config import Settings

from contracts import AbstractIpInfoProvider
from models import IpstackComResponse

class IpStackComProvider(AbstractIpInfoProvider):

    protocol: str = 'https'
    url: str = 'api.ipstack.com'
    settings: Settings

    def __init__(self, settings: Settings):
        self.protocol = 'http'
        self.url = 'api.ipstack.com'
        self.settings = settings

    def get_ip_info(self, ip: str)->IpstackComResponse:
        try:    
            return requests.get(f"{self.protocol}://{self.url}/{ip}?access_key={self.settings.ip_stack_com_access_key}")
        except Exception as e:
            raise e
