class PaymentStrategy:
    def pay(self, amount):
        raise NotImplementedError("This method should be overridden by subclasses.")
class CreditCardPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paying {amount} using Credit Card.")

class PayPalPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paying {amount} using PayPal.")

class CryptoPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paying {amount} using Cryptocurrency.")

class PaymentContext:
    def __init__(self, strategy: PaymentStrategy):
        self._strategy = strategy

    def set_strategy(self, strategy: PaymentStrategy):
        self._strategy = strategy

    def execute_payment(self, amount):
        self._strategy.pay(amount)

if __name__ == "__main__":
    amount = 100  # Сумма платежа

    # Оплата с помощью кредитной карты
    payment_context = PaymentContext(CreditCardPayment())
    payment_context.execute_payment(amount)

    # Изменение стратегии на PayPal
    payment_context.set_strategy(PayPalPayment())
    payment_context.execute_payment(amount)

    # Изменение стратегии на криптовалюту
    payment_context.set_strategy(CryptoPayment())
    payment_context.execute_payment(amount)