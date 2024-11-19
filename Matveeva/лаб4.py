import copy

# Абстрактный класс Graphic
class Graphic:
    def clone(self):
        raise NotImplementedError("Вы должны реализовать этот метод!")

# Класс Circle, наследующий от Graphic
class Circle(Graphic):
    def __init__(self, radius):
        self.radius = radius

    def clone(self):
        return copy.deepcopy(self)  # Клонирование с использованием deepcopy

    def __str__(self):
        return f"Круг с радиусом: {self.radius}"

# Класс Square, наследующий от Graphic
class Square(Graphic):
    def __init__(self, side_length):
        self.side_length = side_length

    def clone(self):
        return copy.deepcopy(self)  # Клонирование с использованием deepcopy

    def __str__(self):
        return f"Квадрат со стороной: {self.side_length}"

# Пример использования
if __name__ == "__main__":
    # Ввод параметров для круга
    radius = float(input("Введите радиус круга: "))
    circle1 = Circle(radius)

    # Ввод параметров для квадрата
    side_length = float(input("Введите длину стороны квадрата: "))
    square1 = Square(side_length)

    # Клонирование объектов
    circle2 = circle1.clone()
    square2 = square1.clone()

    # Изменение параметров клонированных объектов
    new_radius = float(input("Введите новый радиус для клонированного круга: "))
    circle2.radius = new_radius

    new_side_length = float(input("Введите новую длину стороны для клонированного квадрата: "))
    square2.side_length = new_side_length

    # Вывод оригинальных и клонированных объектов
    print(circle1)  # Вывод: Круг с радиусом: <значение>
    print(circle2)  # Вывод: Круг с радиусом: <новое значение>
    print(square1)  # Вывод: Квадрат со стороной: <значение>
    print(square2)  # Вывод: Квадрат со стороной: <новое значение>