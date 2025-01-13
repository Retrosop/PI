class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._initialized = False
        return cls._instance

    def __init__(self, value=None):
        if not self._initialized:
            self.value = value
            self._initialized = True

    @classmethod
    def get_instance(cls):
        
        if cls._instance is None:
            raise Exception("Экземпляр Singleton еще не создан. Используйте Singleton() для создания.")
        return cls._instance

    @classmethod
    def reset_instance(cls):
        """Сбрасывает текущий экземпляр Singleton."""
        cls._instance = None

if __name__ == "__main__":
    singleton1 = Singleton("Первое значение")
    print(f"singleton1 value: {singleton1.value}")

    singleton2 = Singleton.get_instance()
    print(f"singleton2 value: {singleton2.value}")


    Singleton.reset_instance()

   
    try:
        singleton3 = Singleton.get_instance()
    except Exception as e:
        print(f"Ошибка: {e}")

    singleton4 = Singleton("Новое значение")
    print(f"singleton4 value: {singleton4.value}")
