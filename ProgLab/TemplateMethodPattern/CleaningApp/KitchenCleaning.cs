namespace CleaningApp
{
    public class KitchenCleaning : CleaningTemplate
    {
        protected override void PerformCleaning()
        {
            Console.WriteLine("Протираем столешницы на кухне...");
            Console.WriteLine("Чистим раковину...");
            Console.WriteLine("Подметаем и моем пол на кухне.");
        }
    }
}
