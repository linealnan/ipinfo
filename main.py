from fastapi import FastAPI
from config import Settings
from ipstack_com_provider import IpStackComProvider

app = FastAPI()

"""TODO Вынести в DI контейнер"""
settings = Settings(_env_file='.env', _env_file_encoding='utf-8')

"""TODO Вынести в DI контейнер"""
ipinfoprovider = IpStackComProvider(settings)

@app.get("/healcheck")
async def healcheck():
    return {"message": "i'm healthy"}

@app.get("/ipinfo/{ip}")
def get_ip_info(ip: str):
    return {"ip": ipinfoprovider.get_ip_info(ip)}
