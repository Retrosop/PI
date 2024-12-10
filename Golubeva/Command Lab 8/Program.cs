using System;
using System.Collections.Generic;

// Интерфейс команды
public interface ICommand
{
    void Execute();
    void Undo();
}

// Класс, представляющий телевизор
public class Television
{
    public bool IsOn { get; private set; }
    public int CurrentChannel { get; private set; }

    public void TurnOn()
    {
        IsOn = true;
        Console.WriteLine("Телевизор включен.");
    }

    public void TurnOff()
    {
        IsOn = false;
        Console.WriteLine("Телевизор выключен.");
    }

    public void ChangeChannel(int channel)
    {
        if (IsOn)
        {
            CurrentChannel = channel;
            Console.WriteLine($"Канал изменен на {channel}.");
        }
        else
        {
            Console.WriteLine("Телевизор выключен. Невозможно изменить канал.");
        }
    }
}

// Команда включения телевизора
public class TurnOnCommand : ICommand
{
    private Television _television;

    public TurnOnCommand(Television television)
    {
        _television = television;
    }

    public void Execute()
    {
        _television.TurnOn();
    }

    public void Undo()
    {
        _television.TurnOff();
    }
}

// Команда изменения канала
public class ChangeChannelCommand : ICommand
{
    private Television _television;
    private int _newChannel;
    private int _previousChannel;

    public ChangeChannelCommand(Television television, int newChannel)
    {
        _television = television;
        _newChannel = newChannel;
    }

    public void Execute()
    {
        _previousChannel = _television.CurrentChannel;
        _television.ChangeChannel(_newChannel);
    }

    public void Undo()
    {
        _television.ChangeChannel(_previousChannel);
    }
}

// Класс для хранения истории команд
public class CommandHistory
{
    private Stack<ICommand> _history = new Stack<ICommand>();

    public void Push(ICommand command)
    {
        _history.Push(command);
    }

    public ICommand Pop()
    {
        return _history.Pop();
    }

    public bool IsEmpty => _history.Count == 0;
}

// Пример использования
public class Program
{
    public static void Main(string[] args)
    {
        Television tv = new Television();
        CommandHistory history = new CommandHistory();

        // Создаем команды
        ICommand turnOnCommand = new TurnOnCommand(tv);
        ICommand changeChannelCommand1 = new ChangeChannelCommand(tv, 5);
        ICommand changeChannelCommand2 = new ChangeChannelCommand(tv, 10);

        // Выполняем команды
        turnOnCommand.Execute();
        history.Push(turnOnCommand);

        changeChannelCommand1.Execute();
        history.Push(changeChannelCommand1);

        changeChannelCommand2.Execute();
        history.Push(changeChannelCommand2);

        // Отменяем последние две команды
        history.Pop().Undo();
        history.Pop().Undo();

        // Отменяем команду включения телевизора
        history.Pop().Undo();
    }
}