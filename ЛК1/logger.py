from abc import ABC, abstractmethod

class ILogger(ABC):
    @abstractmethod
    def log(self, message: str) -> None:
        pass

class ConsoleLogger(ILogger):
    def log(self, message: str) -> None:
        print(f"Console Logger: {message}")

class FileLogger(ILogger):
    def __init__(self, file_path: str):
        self.file_path = file_path

    def log(self, message: str) -> None:
        with open(self.file_path, 'a') as file:
            file.write(f"File Logger: {message}\n")

class DatabaseLogger(ILogger):
    def log(self, message: str) -> None:
        print(f"Database Logger: {message}")