from abc import ABCMeta, abstractmethod

class AbstractIpInfoProvider(metaclass=ABCMeta):
    @abstractmethod
    def get_ip_info(ip: str):
        pass