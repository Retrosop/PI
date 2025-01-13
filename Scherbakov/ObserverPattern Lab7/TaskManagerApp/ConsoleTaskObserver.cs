using System;

namespace TaskManagerApp
{
    public class ConsoleTaskObserver : ITaskObserver
    {
        public void OnTaskAdded(Task task)
        {
            Console.WriteLine($"[Observer] Task added: {task}");
        }

        public void OnTaskUpdated(Task task)
        {
            Console.WriteLine($"[Observer] Task updated: {task}");
        }

        public void OnTaskRemoved(Task task)
        {
            Console.WriteLine($"[Observer] Task removed: {task}");
        }
    }
}
