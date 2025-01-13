using System;

namespace CleaningApp
{
    public abstract class CleaningTemplate
    {
        // Шаблонный метод
        public void Clean()
        {
            PrepareTools();
            PerformCleaning();
            FinalCheck();
        }

        // Шаги, которые будут одинаковыми для всех
        private void PrepareTools()
        {
            Console.WriteLine("Подготовка инструментов для уборки...");
        }

        private void FinalCheck()
        {
            Console.WriteLine("Финальная проверка убранной комнаты.");
        }

        // Шаги, которые будут различаться в зависимости от комнаты
        protected abstract void PerformCleaning();
    }
}
