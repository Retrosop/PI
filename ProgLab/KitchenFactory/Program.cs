using System;

class Program
{
    static void Main(string[] args)
    {
        Console.WriteLine("Добро пожаловать на кухню!");
        Console.WriteLine("Выберите блюдо для приготовления:");
        Console.WriteLine("1 - Пицца");
        Console.WriteLine("2 - Паста");
        Console.WriteLine("3 - Салат");

        // Получаем выбор пользователя
        Console.Write("Введите ваш выбор (1/2/3): ");
        string? выбор = Console.ReadLine();

        FoodFactory? фабрикаБлюда = null;

        // Выбор блюда
        switch (выбор)
        {
            case "1":
                фабрикаБлюда = new PizzaFactory();
                break;
            case "2":
                фабрикаБлюда = new PastaFactory();
                break;
            case "3":
                фабрикаБлюда = new SaladFactory();
                break;
            default:
                Console.WriteLine("Неверный выбор! Завершаем программу...");
                return; // Завершаем программу
        }

        // Создаём блюдо через выбранную фабрику
        IFood блюдо = фабрикаБлюда.CreateFood();

        // Готовим блюдо
        Console.WriteLine("\nГотовим ваше блюдо...");
        блюдо.Prepare();

        Console.WriteLine("Приятного аппетита!");
    }
}
