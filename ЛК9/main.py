from abc import ABC, abstractmethod


# Базовый класс для всех блюд
class CookingTemplate(ABC):
    def cook(self):
        self.prepare_ingredients()
        self.cook_dish()
        self.serve()

    @abstractmethod
    def prepare_ingredients(self):
        pass

    @abstractmethod
    def cook_dish(self):
        pass

    def serve(self):
        print("Блюдо подано!")


# Класс для супа
class Soup(CookingTemplate):
    def prepare_ingredients(self):
        print("Подготовка овощей и бульона для супа.")

    def cook_dish(self):
        print("Обжарка овощей и варка супа.")


# Класс для пасты
class Pasta(CookingTemplate):
    def prepare_ingredients(self):
        print("Подготовка макарон и соуса.")

    def cook_dish(self):
        print("Отваривание макарон и смешивание соуса.")


# Пример использования
if __name__ == "__main__":
    print("Приготовление супа:")
    soup = Soup()
    soup.cook()

    print("\nПриготовление пасты:")
    pasta = Pasta()
    pasta.cook()