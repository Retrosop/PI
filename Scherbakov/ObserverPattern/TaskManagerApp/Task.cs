namespace TaskManagerApp
{
    public class Task
    {
        public string Title { get; set; }
        public string Description { get; set; }
        public bool IsCompleted { get; set; }

        public Task(string title, string description)
        {
            Title = title;
            Description = description;
            IsCompleted = false;
        }

        public override string ToString()
        {
            return $"[Task] Title: {Title}, Description: {Description}, Completed: {IsCompleted}";
        }
    }
}
