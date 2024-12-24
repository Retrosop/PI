class Pizza:
    def __init__(self, size, dough, toppings):
        self.size = size          # Размер пиццы
        self.dough = dough        # Тип теста
        self.toppings = toppings  # Начинки пиццы

    def __str__(self):
        # Строковое представление объекта Pizza
        return f"Pizza(Size: {self.size}, Dough: {self.dough}, Toppings: {', '.join(self.toppings)})"

class PizzaBuilder:
    def __init__(self):
        self.size = None          # Размер пиццы
        self.dough = None         # Тип теста
        self.toppings = []        # Список начинок

    def set_size(self, size):
        self.size = size          # Установка размера пиццы
        return self               # Возвращаем себя для цепочки вызовов

    def set_dough(self, dough):
        self.dough = dough        # Установка типа теста
        return self               # Возвращаем себя для цепочки вызовов

    def add_topping(self, topping):
        self.toppings.append(topping)  # Добавление начинки
        return self                      # Возвращаем себя для цепочки вызовов

    def build(self):
        # Метод для создания объекта Pizza с заданными параметрами
        return Pizza(self.size, self.dough, self.toppings)


if __name__ == "__main__":
    # Создаем строителя пиццы
    pizza_builder = PizzaBuilder()

    # Поэтапно настраиваем параметры пиццы
    pizza = (pizza_builder
             .set_size("Large")
             .set_dough("Thin crust")
             .add_topping("Cheese")
             .add_topping("Mushrooms")
             .add_topping("Pepperoni")
             .build())  # Создаем пиццу

    # Выводим информацию о созданной пицце
    print(pizza)  # Вывод: Pizza(Size: Large, Dough: Thin crust, Toppings: Cheese, Mushrooms, Pepperoni)