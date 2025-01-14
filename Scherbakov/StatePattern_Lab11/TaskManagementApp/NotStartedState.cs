namespace TaskManagementApp
{
    public class NotStartedState : ITaskState
    {
        public void Start(Task task)
        {
            task.SetState(new InProgressState());
            Console.WriteLine("Задача начата.");
        }

        public void Complete(Task task)
        {
            Console.WriteLine("Задача не может быть завершена, так как она еще не начата.");
        }

        public string GetStatus()
        {
            return "Не начата";
        }
    }
}
