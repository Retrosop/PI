using System;

namespace OrderManagementApp
{
    class Program
    {
        static void Main(string[] args)
        {
            // Создаём коллекцию заказов
            OrderCollection orders = new OrderCollection();

            // Добавляем заказы
            orders.AddOrder(new Order(1, "Alice", 150.00m));
            orders.AddOrder(new Order(2, "Bob", 75.00m));
            orders.AddOrder(new Order(3, "Charlie", 200.00m));
            orders.AddOrder(new Order(4, "David", 50.00m));

            // Фильтруем заказы с суммой выше 100
            Console.WriteLine("Заказы с суммой выше 100:");
            foreach (var order in orders.GetOrdersAboveAmount(100))
            {
                Console.WriteLine(order);
            }

            // Выводим все заказы
            Console.WriteLine("\nВсе заказы:");
            foreach (var order in orders)
            {
                Console.WriteLine(order);
            }
        }
    }
}
