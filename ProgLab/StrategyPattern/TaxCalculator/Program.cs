using System;

namespace TaxCalculator
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Выберите стратегию расчёта налога:");
            Console.WriteLine("1 - Фиксированный процент");
            Console.WriteLine("2 - Прогрессивная шкала");
            Console.Write("Введите ваш выбор: ");
            string choice = Console.ReadLine() ?? "2";

            ITaxStrategy taxStrategy;

            switch (choice)
            {
                case "1":
                    taxStrategy = new FixedTaxStrategy(0.15m); // 15% налог
                    break;
                case "2":
                    taxStrategy = new ProgressiveTaxStrategy();
                    break;
                default:
                    Console.WriteLine("Некорректный выбор. Используется прогрессивная шкала.");
                    taxStrategy = new ProgressiveTaxStrategy();
                    break;
            }

            // Передаём стратегию через конструктор
            TaxContext taxContext = new TaxContext(taxStrategy);

            Console.Write("Введите доход: ");
            if (decimal.TryParse(Console.ReadLine(), out decimal income))
            {
                decimal tax = taxContext.Calculate(income);
                Console.WriteLine($"Ваш налог: {tax:C}");
            }
            else
            {
                Console.WriteLine("Некорректный ввод дохода.");
            }
        }
    }
}
