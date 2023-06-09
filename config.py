from functools import lru_cache

from pydantic import BaseSettings, Field

class Settings(BaseSettings):
    ip_stack_com_access_key: str = ''

class Config:
    env_file = '.env'
    env_file_encoding = 'utf-8'