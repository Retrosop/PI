namespace CleaningApp
{
    public class BathroomCleaning : CleaningTemplate
    {
        protected override void PerformCleaning()
        {
            Console.WriteLine("Чистим ванну...");
            Console.WriteLine("Моем унитаз...");
            Console.WriteLine("Моем пол в ванной.");
        }
    }
}
