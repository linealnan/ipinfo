from typing import Annotated
from fastapi import Depends
import requests
from config import Settings

from contracts import AbstractIpInfoProvider

class IpStackComProvider(AbstractIpInfoProvider, Settings):

    url: str = 'api.ipstack.com'
    protocol: str = 'http'

    @classmethod
    def get_ip_info(self, ip: str):
        return requests.get(f"{self.protocol}://'{self.url}'/'{ip}'?access_key='{Settings.ip_stack_com_access_key}")
