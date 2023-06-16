from fastapi import FastAPI
from config import Settings
from ipstack_com_provider import IpStackComProvider

app = FastAPI(title = "IPinfo")

"""TODO Вынести в DI контейнер"""
settings = Settings(_env_file='.env', _env_file_encoding='utf-8')

"""TODO Вынести в DI контейнер"""
ipinfoprovider = IpStackComProvider(settings)
#print(ipinfoprovider.get_ip_info('46.191.186.238'))

@app.get("/healcheck")
async def healcheck():
    return {"message": "i'm healthy"}

@app.get("/api/v1/ipinfo/{ip}")
def get_ip_info(ip: str):
    return ipinfoprovider.get_ip_info(ip).json()
