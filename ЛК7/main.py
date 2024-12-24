# Определяем класс Subject
class Subject:
    def __init__(self):
        self._observers = []  # Список наблюдателей

    def attach(self, observer):
        """Добавляет наблюдателя в список"""
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer):
        """Удаляет наблюдателя из списка"""
        try:
            self._observers.remove(observer)
        except ValueError:
            pass

    def notify(self, message):
        """Уведомляет всех наблюдателей об изменении"""
        for observer in self._observers:
            observer.update(message)

# Определяем интерфейс наблюдателя
class Observer:
    def update(self, message):
        raise NotImplementedError("Этот метод должен быть переопределён в подклассах.")

# Реализуем несколько конкретных классов наблюдателей
class ConcreteObserverA(Observer):
    def update(self, message):
        print(f"ConcreteObserverA получил уведомление: {message}")

class ConcreteObserverB(Observer):
    def update(self, message):
        print(f"ConcreteObserverB получил уведомление: {message}")

class ConcreteObserverC(Observer):
    def update(self, message):
        print(f"ConcreteObserverC получил уведомление: {message}")

# Пример использования
if __name__ == "__main__":
    # Создаём объект Subject
    subject = Subject()

    # Создаём наблюдателей
    observer_a = ConcreteObserverA()
    observer_b = ConcreteObserverB()
    observer_c = ConcreteObserverC()

    # Присоединяем наблюдателей к объекту Subject
    subject.attach(observer_a)
    subject.attach(observer_b)
    subject.attach(observer_c)

    # Уведомляем всех наблюдателей об изменении
    subject.notify("Изменение произошло!")

    # Удаляем одного наблюдателя и уведомляем снова
    subject.detach(observer_b)
    subject.notify("Другое изменение произошло!")