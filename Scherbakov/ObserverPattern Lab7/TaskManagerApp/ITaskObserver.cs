namespace TaskManagerApp
{
    public interface ITaskObserver
    {
        void OnTaskAdded(Task task);
        void OnTaskUpdated(Task task);
        void OnTaskRemoved(Task task);
    }
}
