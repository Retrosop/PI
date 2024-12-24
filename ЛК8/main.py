# Определяем класс телевидения
class Television:
    def __init__(self):
        self.is_on = False
        self.channel = 1

    def TurnOn(self):
        self.is_on = True
        print("Телевизор включен.")

    def TurnOff(self):
        self.is_on = False
        print("Телевизор выключен.")

    def ChangeChannel(self, channel):
        if not self.is_on:
            print("Телевизор выключен. Невозможно изменить канал.")
            return
        self.channel = channel
        print(f"Канал изменен на {self.channel}.")


# Определяем класс команды
class Command:
    def execute(self):
        raise NotImplementedError("Этот метод должен быть переопределен в подклассах.")


# Реализуем конкретные команды
class TurnOnCommand(Command):
    def __init__(self, television):
        self.television = television

    def execute(self):
        self.television.TurnOn()


class TurnOffCommand(Command):
    def __init__(self, television):
        self.television = television

    def execute(self):
        self.television.TurnOff()


class ChangeChannelCommand(Command):
    def __init__(self, television, channel):
        self.television = television
        self.channel = channel

    def execute(self):
        self.television.ChangeChannel(self.channel)


# Пример использования
if __name__ == "__main__":
    # Создаем объект телевидения
    tv = Television()

    # Создаем команды
    turn_on_command = TurnOnCommand(tv)
    turn_off_command = TurnOffCommand(tv)
    change_channel_command = ChangeChannelCommand(tv, 5)

    # Выполняем команды
    turn_on_command.execute()  # Включаем телевизор
    change_channel_command.execute()  # Меняем канал на 5
    turn_off_command.execute()  # Выключаем телевизор