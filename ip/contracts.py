from abc import ABCMeta, abstractmethod

class AbstractIpInfoRepository(metaclass=ABCMeta):

    @abstractmethod
    def find_by_ip(self, ip: str):
        """Получение данных IP адреса"""
        pass

    @abstractmethod
    def find_and_save_by_ip(self, ip: str):
        """Получение данных IP адреса"""
        pass
