using System;

namespace TaskManagerApp
{
    class Program
    {
        static void Main(string[] args)
        {
            // Создаём менеджер задач
            TaskManager taskManager = new TaskManager();

            // Добавляем наблюдателя
            ConsoleTaskObserver observer = new ConsoleTaskObserver();
            taskManager.AddObserver(observer);

            // Добавляем задачи
            var task1 = new Task("Task 1", "Description of Task 1");
            var task2 = new Task("Task 2", "Description of Task 2");

            taskManager.AddTask(task1);
            taskManager.AddTask(task2);

            // Обновляем задачу
            task1.Description = "Updated description of Task 1";
            task1.IsCompleted = true;
            taskManager.UpdateTask(task1);

            // Удаляем задачу
            taskManager.RemoveTask(task2);
        }
    }
}
