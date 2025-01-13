using System;

class Program
{
    static void Main(string[] args)
    {
        Console.WriteLine("Выберите стиль мебели:");
        Console.WriteLine("1 - Современный");
        Console.WriteLine("2 - Классический");

        Console.Write("Введите ваш выбор (1/2): ");
        string? choice = Console.ReadLine();

        IFurnitureFactory? furnitureFactory = null;

        switch (choice)
        {
            case "1":
                furnitureFactory = new ModernFurnitureFactory();
                break;
            case "2":
                furnitureFactory = new ClassicFurnitureFactory();
                break;
            default:
                Console.WriteLine("Неверный выбор! Завершаем программу...");
                return;
        }

        // Используем фабрику для создания мебели
        var client = new FurnitureClient(furnitureFactory);
        client.CreateFurniture();
    }
}
