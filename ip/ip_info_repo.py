
from ip.contracts import AbstractIpInfoRepository
from ip.sql.queries import IpSqlQueries

class IpInfoRepository(AbstractIpInfoRepository):
    
    def __init__(self, q: IpSqlQueries):
        self.q = q

    def find_by_ip(self, ip: str):
        return self.q.find_by_ip()
