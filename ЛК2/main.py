from abc import ABC, abstractmethod


# Абстрактные классы для предметов мебели
class ITable(ABC):
    @abstractmethod
    def describe(self) -> str:
        pass


class IChair(ABC):
    @abstractmethod
    def describe(self) -> str:
        pass


# Интерфейс фабрики мебели
class IFurnitureFactory(ABC):
    @abstractmethod
    def create_table(self) -> ITable:
        pass

    @abstractmethod
    def create_chair(self) -> IChair:
        pass


# Конкретные реализации стола и стула
class ModernTable(ITable):
    def describe(self) -> str:
        return "Это современный стол."


class ModernChair(IChair):
    def describe(self) -> str:
        return "Это современный стул."


# Конкретная фабрика для производства современной мебели
class ModernFurnitureFactory(IFurnitureFactory):
    def create_table(self) -> ITable:
        return ModernTable()

    def create_chair(self) -> IChair:
        return ModernChair()


# Пример использования
if __name__ == "__main__":
    factory = ModernFurnitureFactory()

    table = factory.create_table()
    table1 = factory.create_table()
    chair = factory.create_chair()
    chair1 = factory.create_chair()

    print(table.describe())
    print(table1.describe())
    print(chair.describe())
    print(chair1.describe())