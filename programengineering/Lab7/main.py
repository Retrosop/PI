# Субъект
class Game:
    def __init__(self):
        self.observers = []  # Список наблюдателей

    def add_observer(self, observer):
        self.observers.append(observer)

    def remove_observer(self, observer):
        self.observers.remove(observer)

    def notify_observers(self, event):
        for observer in self.observers:
            observer.update(event)

    def gain_experience(self, points):
        print(f"Игрок получает {points} очков опыта!")
        self.notify_observers(f"Получено {points} очков опыта")

    def level_up(self, level):
        print(f"Игрок достиг уровня {level}!")
        self.notify_observers(f"Достигнут уровень {level}")


# Интерфейс наблюдателя
class Observer:
    def update(self, event):
        raise NotImplementedError("Этот метод должен быть реализован в подклассе")


# Конкретные наблюдатели
class Achievements(Observer):
    def update(self, event):
        print(f"[Достижения] Обновление: {event}")


class Logger(Observer):
    def update(self, event):
        print(f"[Журнал] Запись события: {event}")


class Notifications(Observer):
    def update(self, event):
        print(f"[Уведомление игроку] Событие: {event}")



if __name__ == "__main__":
    game = Game()

    achievements = Achievements()
    logger = Logger()
    notifications = Notifications()

    game.add_observer(achievements)
    game.add_observer(logger)
    game.add_observer(notifications)

    game.gain_experience(100)
    game.level_up(2)

    game.remove_observer(logger)
    print("\n[Журнал больше не будет записывать события]\n")

    game.gain_experience(200)
    game.level_up(3)
