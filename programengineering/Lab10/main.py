from datetime import datetime
from typing import List, Iterator


class Project:
    def __init__(self, name: str, start_date: str, end_date: str):
        self.name = name
        self.start_date = datetime.strptime(start_date, "%Y-%m-%d")
        self.end_date = datetime.strptime(end_date, "%Y-%m-%d")

    def __str__(self):
        return f"Проект: {self.name}, Начало: {self.start_date.date()}, Конец: {self.end_date.date()}"


class ProjectIterator:
    def __init__(self, projects: List[Project], start_period: str, end_period: str):
        self.projects = projects
        self.start_period = datetime.strptime(start_period, "%Y-%m-%d")
        self.end_period = datetime.strptime(end_period, "%Y-%m-%d")
        self.index = 0

    def __iter__(self) -> Iterator[Project]:
        return self

    def __next__(self) -> Project:
        while self.index < len(self.projects):
            project = self.projects[self.index]
            self.index += 1
            if self.start_period <= project.start_date <= self.end_period:
                return project
        raise StopIteration


if __name__ == "__main__":
    projects = [
        Project("Проект А", "2023-01-10", "2023-06-15"),
        Project("Проект Б", "2023-05-01", "2023-09-20"),
        Project("Проект В", "2024-01-01", "2024-07-30"),
        Project("Проект Г", "2022-11-15", "2023-03-10"),
        Project("Проект Д", "2023-03-05", "2023-08-25"),
        Project("Проект Е", "2024-05-10", "2024-11-15"),
        Project("Проект Ж", "2023-07-01", "2023-12-20"),
        Project("Проект З", "2022-08-20", "2023-02-10"),
        Project("Проект И", "2023-09-10", "2024-01-15"),
        Project("Проект К", "2023-12-01", "2024-04-30"),
    ]

    start_period = "2023-01-01"
    end_period = "2023-12-31"

    print(f"Проекты, начавшиеся в период с {start_period} по {end_period}:")
    project_iterator = ProjectIterator(projects, start_period, end_period)
    for project in project_iterator:
        print(project)
