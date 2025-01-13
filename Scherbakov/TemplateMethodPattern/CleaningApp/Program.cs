using System;

namespace CleaningApp
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Уборка кухни:");
            CleaningTemplate kitchenCleaning = new KitchenCleaning();
            kitchenCleaning.Clean();

            Console.WriteLine("\nУборка ванной комнаты:");
            CleaningTemplate bathroomCleaning = new BathroomCleaning();
            bathroomCleaning.Clean();
        }
    }
}
