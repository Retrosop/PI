using System;

namespace TaskManagementApp
{
    public class Task
    {
        public string Title { get; private set; }
        private ITaskState _state;

        public Task(string title)
        {
            Title = title;
            _state = new NotStartedState(); // Задача изначально находится в состоянии "Не начата"
        }

        public void SetState(ITaskState state)
        {
            _state = state;
        }

        public void Start()
        {
            _state.Start(this);
        }

        public void Complete()
        {
            _state.Complete(this);
        }

        public void DisplayStatus()
        {
            Console.WriteLine($"Статус задачи '{Title}': {_state.GetStatus()}");
        }
    }
}
