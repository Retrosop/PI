class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

    def __init__(self, value=None):
        if not hasattr(self, 'initialized'):  # Проверка на инициализацию
            self.value = value
            self.initialized = True

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            raise Exception("Instance not created yet.")
        return cls._instance

# Пример использования
if __name__ == "__main__":
    singleton1 = Singleton("Первый экземпляр")
    print(singleton1.value)  # Вывод: Первый экземпляр

    singleton2 = Singleton("Второй экземпляр")
    print(singleton2.value)  # Вывод: Первый экземпляр, так как это тот же экземпляр

    # Проверка на null
    instance = Singleton.get_instance()
    print(instance.value)  # Вывод: Первый экземпляр

    # Проверка на случай, если экземпляр не был создан
    Singleton._instance = None  # Удаляем экземпляр
    try:
        Singleton.get_instance()  # Это вызовет исключение
    except Exception as e:
        print(e)  # Вывод: Instance not created yet.