from logger_factory import LoggerFactory, LoggerType


def main():
    # Создание и использование различных логгеров
    console_logger = LoggerFactory.create_logger(LoggerType.CONSOLE)
    console_logger.log("This is a message for the console.")

    file_logger = LoggerFactory.create_logger(LoggerType.FILE, "log.txt")
    file_logger.log("This is a message for the file.")

    database_logger = LoggerFactory.create_logger(LoggerType.DATABASE)
    database_logger.log("This is a message for the database.")


if __name__ == "__main__":
    main()