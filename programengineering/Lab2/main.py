from abc import ABC, abstractmethod

# Интерфейсы для продуктов
class ITable(ABC):
    @abstractmethod
    def material(self):
        pass

    @abstractmethod
    def style(self):
        pass

    @abstractmethod
    def description(self):
        pass


class IChair(ABC):
    @abstractmethod
    def has_armrests(self):
        pass

    @abstractmethod
    def style(self):
        pass

    @abstractmethod
    def description(self):
        pass



class VictorianTable(ITable):
    def material(self):
        return "Дерево с резными орнаментами"

    def style(self):
        return "Викторианский"

    def description(self):
        return "Роскошный стол, выполненный в классическом викторианском стиле. Его утончённые резные детали и высококачественное дерево делают его идеальным для создания атмосферы эпохи XIX века."


class VictorianChair(IChair):
    def has_armrests(self):
        return True

    def style(self):
        return "Викторианский"

    def description(self):
        return "Элегантный стул, сочетающий комфорт и изысканность. Подходит для классических интерьеров, где ценится внимание к деталям."



class ModernTable(ITable):
    def material(self):
        return "Стекло и металл"

    def style(self):
        return "Современный"

    def description(self):
        return "Лаконичный стол с минималистичным дизайном. Металлический каркас и стеклянная столешница делают его идеальным для современных интерьеров с акцентом на простоту и функциональность."


class ModernChair(IChair):
    def has_armrests(self):
        return False

    def style(self):
        return "Современный"

    def description(self):
        return "Удобный стул с лаконичным дизайном. Идеально подходит для современных пространств, где важны эргономика и стиль."


class IFurnitureFactory(ABC):
    @abstractmethod
    def create_table(self):
        pass

    @abstractmethod
    def create_chair(self):
        pass
class VictorianFurnitureFactory(IFurnitureFactory):
    def create_table(self):
        return VictorianTable()

    def create_chair(self):
        return VictorianChair()


class ModernFurnitureFactory(IFurnitureFactory):
    def create_table(self):
        return ModernTable()

    def create_chair(self):
        return ModernChair()


def get_furniture(factory: IFurnitureFactory):
    table = factory.create_table()
    chair = factory.create_chair()

    print(f"Стиль стола: {table.style()}, Материал: {table.material()}")
    print(f"Описание: {table.description()}")
    print(f"Стиль стула: {chair.style()}, Наличие подлокотников: {chair.has_armrests()}")
    print(f"Описание: {chair.description()}")


if __name__ == "__main__":
    print("Викторианская мебель:")
    victorian_factory = VictorianFurnitureFactory()
    get_furniture(victorian_factory)

    print("\nСовременная мебель:")
    modern_factory = ModernFurnitureFactory()
    get_furniture(modern_factory)
