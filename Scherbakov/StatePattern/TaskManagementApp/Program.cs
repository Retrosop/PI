using System;

namespace TaskManagementApp
{
    class Program
    {
        static void Main(string[] args)
        {
            // Создаём задачу
            Task task = new Task("Написать отчет");

            // Проверяем статус задачи
            task.DisplayStatus();

            // Пытаемся завершить задачу, которая еще не начата
            task.Complete();

            // Начинаем задачу
            task.Start();

            // Проверяем статус
            task.DisplayStatus();

            // Завершаем задачу
            task.Complete();

            // Проверяем статус
            task.DisplayStatus();

            // Пытаемся начать завершенную задачу
            task.Start();
        }
    }
}
