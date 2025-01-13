class Command:
    def execute(self):
        raise NotImplementedError("Этот метод должен быть реализован в подклассе")


class TurnOnTVCommand(Command):
    def __init__(self, tv):
        self.tv = tv

    def execute(self):
        self.tv.turn_on()


class SetChannelCommand(Command):
    def __init__(self, tv, channel):
        self.tv = tv
        self.channel = channel

    def execute(self):
        self.tv.set_channel(self.channel)


class IncreaseVolumeCommand(Command):
    def __init__(self, tv, amount):
        self.tv = tv
        self.amount = amount

    def execute(self):
        self.tv.increase_volume(self.amount)

class TV:
    def __init__(self):
        self.is_on = False
        self.channel = None
        self.volume = 10

    def turn_on(self):
        self.is_on = True
        print("Телевизор включён.")

    def set_channel(self, channel):
        if self.is_on:
            self.channel = channel
            print(f"Канал установлен на {channel}.")
        else:
            print("Телевизор выключен. Невозможно установить канал.")

    def increase_volume(self, amount):
        if self.is_on:
            self.volume += amount
            print(f"Громкость увеличена на {amount}. Текущая громкость: {self.volume}.")
        else:
            print("Телевизор выключен. Невозможно изменить громкость.")


# Класс MacroCommand для выполнения нескольких команд
class MacroCommand(Command):
    def __init__(self, commands):
        self.commands = commands

    def execute(self):
        for command in self.commands:
            command.execute()


if __name__ == "__main__":
    tv = TV()

    turn_on_command = TurnOnTVCommand(tv)
    set_channel_command = SetChannelCommand(tv, 5)
    increase_volume_command = IncreaseVolumeCommand(tv, 15)

    macro_command = MacroCommand([turn_on_command, set_channel_command, increase_volume_command])

    print("Выполнение макрокоманды:")
    macro_command.execute()
