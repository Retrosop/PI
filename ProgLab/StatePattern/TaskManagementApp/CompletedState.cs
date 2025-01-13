namespace TaskManagementApp
{
    public class CompletedState : ITaskState
    {
        public void Start(Task task)
        {
            Console.WriteLine("Задача уже завершена и не может быть начата заново.");
        }

        public void Complete(Task task)
        {
            Console.WriteLine("Задача уже завершена.");
        }

        public string GetStatus()
        {
            return "Завершена";
        }
    }
}
