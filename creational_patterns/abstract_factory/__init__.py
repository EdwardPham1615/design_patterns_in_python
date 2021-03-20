from __future__ import annotations
from abc import ABC, abstractmethod


class FurnitureFactory(ABC):
    @abstractmethod
    def create_chair(self) -> Chair:
        pass

    @abstractmethod
    def create_sofa(self) -> Sofa:
        pass


class VictorianFurnitureFactory(FurnitureFactory):

    def create_chair(self) -> Chair:
        return VictorianChair()

    def create_sofa(self) -> Sofa:
        return VictorianSofa()


class ModernFurnitureFactory(FurnitureFactory):

    def create_chair(self) -> Chair:
        return ModernChair()

    def create_sofa(self) -> Sofa:
        return ModernSofa()


class Chair(ABC):
    @abstractmethod
    def type(self) -> str:
        pass


class Sofa(ABC):
    @abstractmethod
    def type(self) -> str:
        pass


class VictorianChair(Chair):
    def type(self) -> str:
        return "This is Victorian Chair"


class VictorianSofa(Sofa):
    def type(self) -> str:
        return "This is Victorian Sofa"


class ModernChair(Chair):
    def type(self) -> str:
        return "This is Modern Chair"


class ModernSofa(Sofa):
    def type(self) -> str:
        return "This is Modern Sofa"
