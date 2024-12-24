from enum import Enum
from logger import ConsoleLogger, FileLogger, DatabaseLogger, ILogger

class LoggerType(Enum):
    CONSOLE = 1
    FILE = 2
    DATABASE = 3

class LoggerFactory:
    @staticmethod
    def create_logger(logger_type: LoggerType, file_path: str = None) -> ILogger:
        if logger_type == LoggerType.CONSOLE:
            return ConsoleLogger()
        elif logger_type == LoggerType.FILE:
            if file_path is None:
                raise ValueError("File path must be provided for FileLogger")
            return FileLogger(file_path)
        elif logger_type == LoggerType.DATABASE:
            return DatabaseLogger()
        else:
            raise ValueError("Invalid logger type")