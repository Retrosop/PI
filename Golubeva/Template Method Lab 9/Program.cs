using System;

// Базовый класс, определяющий общий алгоритм покупки
abstract class PurchaseProcess
{
    // Шаблонный метод, который определяет последовательность шагов
    public void Purchase()
    {
        SelectProduct();
        AddToCart();
        Checkout();
        ProcessPayment();
        CompleteOrder();
    }

    // Шаги, которые могут быть переопределены подклассами
    protected virtual void SelectProduct()
    {
        Console.WriteLine("Выбор товара...");
    }

    protected virtual void AddToCart()
    {
        Console.WriteLine("Добавление товара в корзину...");
    }

    protected virtual void Checkout()
    {
        Console.WriteLine("Оформление заказа...");
    }

    // Абстрактный метод, который должен быть реализован в подклассах
    protected abstract void ProcessPayment();

    protected virtual void CompleteOrder()
    {
        Console.WriteLine("Заказ оформлен.");
    }
}

// Подкласс для оплаты кредитной картой
class CreditCardPurchase : PurchaseProcess
{
    protected override void ProcessPayment()
    {
        Console.WriteLine("Оплата кредитной картой...");
    }
}

// Подкласс для оплаты через PayPal
class PayPalPurchase : PurchaseProcess
{
    protected override void ProcessPayment()
    {
        Console.WriteLine("Оплата через PayPal...");
    }
}

// Пример использования
class Program
{
    static void Main(string[] args)
    {
        Console.WriteLine("Покупка с использованием кредитной карты:");
        PurchaseProcess creditCardPurchase = new CreditCardPurchase();
        creditCardPurchase.Purchase();

        Console.WriteLine("\nПокупка с использованием PayPal:");
        PurchaseProcess payPalPurchase = new PayPalPurchase();
        payPalPurchase.Purchase();
    }
}