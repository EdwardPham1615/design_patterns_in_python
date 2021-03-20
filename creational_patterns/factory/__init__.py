from __future__ import annotations
from abc import ABC, abstractmethod


class LogisticsFactory(ABC):
    @abstractmethod
    def create_transport(self):
        pass

    def operation(self):
        transport = self.create_transport()
        result = f"Please wait a minute. {transport}"
        return result


class RoadLogistics(LogisticsFactory):
    def create_transport(self) -> Transport:
        return CreateRoadTransport()


class SeaLogistics(LogisticsFactory):
    def create_transport(self) -> Transport:
        return CreateSeaTransport()


class Transport(ABC):
    @abstractmethod
    def get_transport(self):
        pass


class CreateRoadTransport(Transport):
    def get_transport(self):
        return "Truck is coming !!!"


class CreateSeaTransport(Transport):
    def get_transport(self):
        return "Ship is coming !!!"
