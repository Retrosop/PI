from abc import ABC, abstractmethod

class TestTemplate(ABC):
    def run_test(self):
        """Общий процесс тестирования"""
        self.prepare_environment()
        self.execute_test()
        self.analyze_results()

    @abstractmethod
    def prepare_environment(self):
        pass

    @abstractmethod
    def execute_test(self):
        pass

    @abstractmethod
    def analyze_results(self):
        pass


class UnitTest(TestTemplate):
    def prepare_environment(self):
        print("Подготовка окружения для юнит-тестов...")

    def execute_test(self):
        print("Выполнение юнит-тестов...")

    def analyze_results(self):
        print("Анализ результатов юнит-тестов.")


class IntegrationTest(TestTemplate):
    def prepare_environment(self):
        print("Настройка базы данных и сервисов для интеграционных тестов...")

    def execute_test(self):
        print("Запуск интеграционных тестов...")

    def analyze_results(self):
        print("Проверка связности компонентов и анализа логов.")


if __name__ == "__main__":
    print("=== Юнит-тесты ===")
    unit_test = UnitTest()
    unit_test.run_test()

    print("\n=== Интеграционные тесты ===")
    integration_test = IntegrationTest()
    integration_test.run_test()
