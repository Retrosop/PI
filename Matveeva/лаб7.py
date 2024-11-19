from abc import ABC, abstractmethod

# Интерфейс наблюдателя
class Observer(ABC):
    @abstractmethod
    def update(self, currency: str, rate: float):
        pass

# Класс для отслеживания курсов валют
class CurrencyExchange:
    def __init__(self):
        self._observers = []
        self._rates = {}

    def attach(self, observer: Observer):
        self._observers.append(observer)

    def detach(self, observer: Observer):
        self._observers.remove(observer)

    def notify(self, currency: str, rate: float):
        for observer in self._observers:
            observer.update(currency, rate)

    def set_rate(self, currency: str, rate: float):
        # Уведомляем наблюдателей только о значительных изменениях
        if currency in self._rates:
            if abs(rate - self._rates[currency]) >= 0.1:  # Порог изменения
                self._rates[currency] = rate
                self.notify(currency, rate)
        else:
            self._rates[currency] = rate
            self.notify(currency, rate)

# Конкретный наблюдатель
class CurrencyObserver(Observer):
    def __init__(self, name: str):
        self.name = name

    def update(self, currency: str, rate: float):
        print(f"{self.name} получил уведомление: Курс {currency} изменился на {rate:.2f}")

# Пример использования
if __name__ == "__main__":
    exchange = CurrencyExchange()

    observer1 = CurrencyObserver("Наблюдатель 1")
    observer2 = CurrencyObserver("Наблюдатель 2")

    exchange.attach(observer1)
    exchange.attach(observer2)

    # Устанавливаем курсы валют
    exchange.set_rate("USD", 75.50)
    exchange.set_rate("EUR", 85.30)
    exchange.set_rate("USD", 75.60)  # Значительное изменение
    exchange.set_rate("EUR", 85.20)  # Не значительное изменение
    exchange.set_rate("USD", 75.80)  # Значительное изменение
    