from sqlalchemy import String
from sqlalchemy.orm import Session

from . import models

class IpSqlQueries():

    def find_by_ip(db: Session, ip: String):
        """ Поиск метаданных по ip """
        return db.query(models.IpInfo).filter(models.IpInfo.ip == ip).first()