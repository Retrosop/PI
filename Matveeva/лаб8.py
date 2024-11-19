import tkinter as tk
from abc import ABC, abstractmethod

# Интерфейс команды
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

# Команды для телевизора
class TVOnCommand(Command):
    def __init__(self, indicator):
        self.indicator = indicator

    def execute(self):
        print("Телевизор включен.")
        self.indicator.config(bg='green')  # Индикатор зеленый

class TVOffCommand(Command):
    def __init__(self, indicator):
        self.indicator = indicator

    def execute(self):
        print("Телевизор выключен.")
        self.indicator.config(bg='red')  # Индикатор красный

class TVVolumeUpCommand(Command):
    def __init__(self, volume_label):
        self.volume_label = volume_label

    def execute(self):
        current_volume = int(self.volume_label["text"])
        if current_volume < 10:
            current_volume += 1
            self.volume_label["text"] = str(current_volume)
            print(f"Громкость телевизора: {current_volume}")

class TVVolumeDownCommand(Command):
    def __init__(self, volume_label):
        self.volume_label = volume_label

    def execute(self):
        current_volume = int(self.volume_label["text"])
        if current_volume > 0:
            current_volume -= 1
            self.volume_label["text"] = str(current_volume)
            print(f"Громкость телевизора: {current_volume}")

# Команды для автомобиля
class CarStartCommand(Command):
    def __init__(self, indicator):
        self.indicator = indicator

    def execute(self):
        print("Автомобиль заведен.")
        self.indicator.config(bg='green')  # Индикатор зеленый

class CarStopCommand(Command):
    def __init__(self, indicator):
        self.indicator = indicator

    def execute(self):
        print("Автомобиль остановлен.")
        self.indicator.config(bg='red')  # Индикатор красный

class CarHornCommand(Command):
    def execute(self):
        print("Гудок автомобиля.")

# Класс для создания интерфейса
class RemoteControlApp:
    def __init__(self, master):
        self.master = master
        master.title("Пульт управления")
        master.geometry("270x380")  # Фиксированный размер окна

        # Инициализация громкости
        self.tv_volume = 0

        # Индикаторы
        self.indicator_frame = tk.Frame(master)
        self.indicator_frame.pack(pady=10)

        # Индикатор телевизора
        self.tv_indicator = tk.Label(self.indicator_frame, width=5, height=2, bg='red')  # Красный по умолчанию
        self.tv_indicator.grid(row=0, column=0)

        self.tv_label = tk.Label(self.indicator_frame, text="Телевизор", font=("Arial", 12))
        self.tv_label.grid(row=0, column=1, padx=10)

        # Индикатор автомобиля
        self.car_indicator = tk.Label(self.indicator_frame, width=5, height=2, bg='red')  # Красный по умолчанию
        self.car_indicator.grid(row=1, column=0)

        self.car_label = tk.Label(self.indicator_frame, text="Автомобиль", font=("Arial", 12))
        self.car_label.grid(row=1, column=1, padx=10)

        # Команды для телевизора
        self.tv_on = TVOnCommand(self.tv_indicator)
        self.tv_off = TVOffCommand(self.tv_indicator)
        
        # Метка для отображения громкости
        self.volume_label = tk.Label(master, text=str(self.tv_volume), font=("Arial", 24))
        self.volume_label.pack(pady=10)

        self.tv_volume_up = TVVolumeUpCommand(self.volume_label)
        self.tv_volume_down = TVVolumeDownCommand(self.volume_label)

        # Команды для автомобиля
        self.car_start = CarStartCommand(self.car_indicator)
        self.car_stop = CarStopCommand(self.car_indicator)
        self.car_horn = CarHornCommand()

        # Кнопки для телевизора
        button_width = 20  # Ширина кнопок

        self.tv_on_button = tk.Button(master, text="Включить телевизор", width=button_width, command=self.tv_on.execute)
        self.tv_on_button.pack(pady=5)

        self.tv_off_button = tk.Button(master, text="Выключить телевизор", width=button_width, command=self.tv_off.execute)
        self.tv_off_button.pack(pady=5)

        # Кнопки громкости на одной строке
        volume_frame = tk.Frame(master)
        volume_frame.pack(pady=5)

        self.tv_volume_up_button = tk.Button(volume_frame, text="+", width=10, command=self.tv_volume_up.execute)
        self.tv_volume_up_button.pack(side=tk.LEFT)

        self.tv_volume_down_button = tk.Button(volume_frame, text="-", width=10, command=self.tv_volume_down.execute)
        self.tv_volume_down_button.pack(side=tk.LEFT)

        # Кнопки для автомобиля
        self.car_start_button = tk.Button(master, text="Завести автомобиль", width=button_width, command=self.car_start.execute)
        self.car_start_button.pack(pady=5)

        self.car_stop_button = tk.Button(master, text="Остановить автомобиль", width=button_width, command=self.car_stop.execute)
        self.car_stop_button.pack(pady=5)

        self.car_horn_button = tk.Button(master, text="Гудок", width=button_width, command=self.car_horn.execute)
        self.car_horn_button.pack(pady=5)

# Запуск приложения
if __name__ == "__main__":
    root = tk.Tk()
    app = RemoteControlApp(root)
    root.mainloop()