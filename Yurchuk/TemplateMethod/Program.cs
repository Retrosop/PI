using System;

namespace TemplateMethodPattern
{
    // Базовый класс, задающий общий алгоритм организации мероприятия
    abstract class EventOrganizer
    {
        // Шаблонный метод: определяет общий процесс
        public void OrganizeEvent()
        {
            PlanEvent();
            PrepareEvent();
            ConductEvent();
            WrapUpEvent();
        }

        // Общий шаг: планирование
        protected abstract void PlanEvent();

        // Общий шаг: подготовка
        protected abstract void PrepareEvent();

        // Общий шаг: проведение
        protected abstract void ConductEvent();

        // Общий шаг: завершение
        protected virtual void WrapUpEvent()
        {
            Console.WriteLine("Завершение мероприятия. Спасибо за участие!");
        }
    }

    // Подкласс для организации свадеб
    class WeddingOrganizer : EventOrganizer
    {
        protected override void PlanEvent()
        {
            Console.WriteLine("Планируем свадьбу: выбор места, составление списка гостей, разработка программы.");
        }

        protected override void PrepareEvent()
        {
            Console.WriteLine("Готовим свадьбу: бронирование зала, заказ цветов и тортов, украшение.");
        }

        protected override void ConductEvent()
        {
            Console.WriteLine("Проводим свадьбу: регистрация брака, банкет, танцы.");
        }
    }

    // Подкласс для организации корпоративов
    class CorporateEventOrganizer : EventOrganizer
    {
        protected override void PlanEvent()
        {
            Console.WriteLine("Планируем корпоратив: выбор темы, составление расписания, определение бюджета.");
        }

        protected override void PrepareEvent()
        {
            Console.WriteLine("Готовим корпоратив: бронирование конференц-зала, подготовка оборудования, согласование меню.");
        }

        protected override void ConductEvent()
        {
            Console.WriteLine("Проводим корпоратив: деловые доклады, тимбилдинг, ужин.");
        }
    }

    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Организация свадьбы:");
            EventOrganizer weddingOrganizer = new WeddingOrganizer();
            weddingOrganizer.OrganizeEvent();

            Console.WriteLine("\nОрганизация корпоратива:");
            EventOrganizer corporateOrganizer = new CorporateEventOrganizer();
            corporateOrganizer.OrganizeEvent();
        }
    }
}