class Logger:
    _instance = None  # Поле для хранения единственного экземпляра класса

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Logger, cls).__new__(cls)  # Создаем новый экземпляр
            cls._instance.log_file = 'log.txt'  # Файл для записи логов
        return cls._instance

    def log(self, message: str) -> None:
        with open(self.log_file, 'a') as file:
            file.write(message + '\n')

# Пример использования
if __name__ == "__main__":
    logger1 = Logger()
    logger2 = Logger()

    # Проверим, что оба экземпляра одинаковы
    print(f"logger1: {id(logger1)}")
    print(f"logger2: {id(logger2)}")

    # Запись логов
    logger1.log("Это первое сообщение лога.")
    logger2.log("Это второе сообщение лога.")