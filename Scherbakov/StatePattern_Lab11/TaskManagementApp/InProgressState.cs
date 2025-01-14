namespace TaskManagementApp
{
    public class InProgressState : ITaskState
    {
        public void Start(Task task)
        {
            Console.WriteLine("Задача уже в процессе выполнения.");
        }

        public void Complete(Task task)
        {
            task.SetState(new CompletedState());
            Console.WriteLine("Задача завершена.");
        }

        public string GetStatus()
        {
            return "В процессе выполнения";
        }
    }
}
