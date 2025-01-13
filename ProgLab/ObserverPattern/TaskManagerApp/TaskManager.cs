using System;
using System.Collections.Generic;

namespace TaskManagerApp
{
    public class TaskManager
    {
        private readonly List<Task> _tasks = new();
        private readonly List<ITaskObserver> _observers = new();

        public void AddObserver(ITaskObserver observer)
        {
            _observers.Add(observer);
        }

        public void RemoveObserver(ITaskObserver observer)
        {
            _observers.Remove(observer);
        }

        public void AddTask(Task task)
        {
            _tasks.Add(task);
            NotifyTaskAdded(task);
        }

        public void UpdateTask(Task task)
        {
            var existingTask = _tasks.Find(t => t.Title == task.Title);
            if (existingTask != null)
            {
                existingTask.Description = task.Description;
                existingTask.IsCompleted = task.IsCompleted;
                NotifyTaskUpdated(existingTask);
            }
        }

        public void RemoveTask(Task task)
        {
            if (_tasks.Remove(task))
            {
                NotifyTaskRemoved(task);
            }
        }

        private void NotifyTaskAdded(Task task)
        {
            foreach (var observer in _observers)
            {
                observer.OnTaskAdded(task);
            }
        }

        private void NotifyTaskUpdated(Task task)
        {
            foreach (var observer in _observers)
            {
                observer.OnTaskUpdated(task);
            }
        }

        private void NotifyTaskRemoved(Task task)
        {
            foreach (var observer in _observers)
            {
                observer.OnTaskRemoved(task);
            }
        }
    }
}
