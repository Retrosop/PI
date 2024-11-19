from abc import ABC, abstractmethod
from datetime import datetime
from typing import List

# Класс задачи
class Task:
    def __init__(self, name: str, priority: int, due_date: datetime, complexity: int):
        self.name = name
        self.priority = priority
        self.due_date = due_date
        self.complexity = complexity

    def __repr__(self):
        return f"Task(name={self.name}, priority={self.priority}, due_date={self.due_date}, complexity={self.complexity})"

# Интерфейс стратегии
class SortingStrategy(ABC):
    @abstractmethod
    def sort(self, tasks: List[Task]) -> List[Task]:
        pass

# Стратегия сортировки по приоритету
class SortByPriority(SortingStrategy):
    def sort(self, tasks: List[Task]) -> List[Task]:
        return sorted(tasks, key=lambda task: task.priority)

# Стратегия сортировки по срокам
class SortByDueDate(SortingStrategy):
    def sort(self, tasks: List[Task]) -> List[Task]:
        return sorted(tasks, key=lambda task: task.due_date)

# Стратегия сортировки по сложности
class SortByComplexity(SortingStrategy):
    def sort(self, tasks: List[Task]) -> List[Task]:
        return sorted(tasks, key=lambda task: task.complexity)

# Контекст, который использует стратегию
class TaskManager:
    def __init__(self, strategy: SortingStrategy):
        self.strategy = strategy

    def set_strategy(self, strategy: SortingStrategy):
        self.strategy = strategy

    def sort_tasks(self, tasks: List[Task]) -> List[Task]:
        return self.strategy.sort(tasks)

# Пример использования
if __name__ == "__main__":
    tasks = [
        Task("Задача 1", priority=2, due_date=datetime(2024, 11, 20), complexity=3),
        Task("Задача 2", priority=1, due_date=datetime(2024, 11, 15), complexity=2),
        Task("Задача 3", priority=3, due_date=datetime(2024, 11, 10), complexity=1),
    ]

    # Создаем менеджер задач с начальной стратегией
    task_manager = TaskManager(SortByPriority())

    print("Сортировка по приоритету:")
    sorted_tasks = task_manager.sort_tasks(tasks)
    print(sorted_tasks)

    # Меняем стратегию на сортировку по срокам
    task_manager.set_strategy(SortByDueDate())
    print("\nСортировка по срокам:")
    sorted_tasks = task_manager.sort_tasks(tasks)
    print(sorted_tasks)

    # Меняем стратегию на сортировку по сложности
    task_manager.set_strategy(SortByComplexity())
    print("\nСортировка по сложности:")
    sorted_tasks = task_manager.sort_tasks(tasks)
    print(sorted_tasks)