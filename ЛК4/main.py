import copy


class Shape:
    def __init__(self, color, size):
        self.color = color  # Цвет фигуры
        self.size = size  # Размер фигуры

    def clone(self):
        # Метод для клонирования объекта Shape
        return copy.deepcopy(self)

    def __str__(self):
        # Возвращает строковое представление объекта
        return f"Shape(Color: {self.color}, Size: {self.size})"


# Пример использования
if __name__ == "__main__":
    # Создаем экземпляр класса Shape
    shape1 = Shape("Red", 10)

    # Клонируем shape1 в shape2
    shape2 = shape1.clone()

    # Изменяем свойства клона
    shape2.color = "Blue"
    shape2.size = 15

    # Выводим информацию о каждом объекте
    print(shape1)  # Вывод: Shape(Color: Red, Size: 10)
    print(shape2)  # Вывод: Shape(Color: Blue, Size: 15)