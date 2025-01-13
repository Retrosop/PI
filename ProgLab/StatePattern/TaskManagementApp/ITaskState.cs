namespace TaskManagementApp
{
    public interface ITaskState
    {
        void Start(Task task);
        void Complete(Task task);
        string GetStatus();
    }
}
