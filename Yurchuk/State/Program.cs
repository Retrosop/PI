using System;

// Интерфейс состояния
public interface ICharacterState
{
    void HandleInput(Character character, string action);
    void Update();
}

// Конкретное состояние: Бездействие (Idle)
public class IdleState : ICharacterState
{
    public void HandleInput(Character character, string action)
    {
        if (action == "Run")
        {
            Console.WriteLine("Персонаж начинает бежать...");
            character.SetState(new RunningState());
        }
        else if (action == "Attack")
        {
            Console.WriteLine("Персонаж начинает атаковать...");
            character.SetState(new AttackingState());
        }
    }

    public void Update()
    {
        Console.WriteLine("Персонаж в состоянии: Бездействие (Idle).");
    }
}

// Конкретное состояние: Бег (Running)
public class RunningState : ICharacterState
{
    public void HandleInput(Character character, string action)
    {
        if (action == "Stop")
        {
            Console.WriteLine("Персонаж останавливается...");
            character.SetState(new IdleState());
        }
        else if (action == "Attack")
        {
            Console.WriteLine("Персонаж начинает атаковать во время бега...");
            character.SetState(new AttackingState());
        }
    }

    public void Update()
    {
        Console.WriteLine("Персонаж в состоянии: Бег (Running).");
    }
}

// Конкретное состояние: Атака (Attacking)
public class AttackingState : ICharacterState
{
    public void HandleInput(Character character, string action)
    {
        if (action == "Stop")
        {
            Console.WriteLine("Персонаж завершает атаку и останавливается...");
            character.SetState(new IdleState());
        }
        else if (action == "Run")
        {
            Console.WriteLine("Персонаж переходит к бегу после атаки...");
            character.SetState(new RunningState());
        }
    }

    public void Update()
    {
        Console.WriteLine("Персонаж в состоянии: Атака (Attacking).");
    }
}

// Класс персонажа
public class Character
{
    private ICharacterState _currentState;

    public Character()
    {
        // Начальное состояние - Idle
        _currentState = new IdleState();
    }

    public void SetState(ICharacterState state)
    {
        _currentState = state;
    }

    public void HandleInput(string action)
    {
        _currentState.HandleInput(this, action);
    }

    public void Update()
    {
        _currentState.Update();
    }
}

// Тестирование с вводом команд
class Program
{
    static void Main()
    {
        Character character = new Character();

        // Вывод доступных команд
        Console.WriteLine("Добро пожаловать в симуляцию игрового персонажа!");
        Console.WriteLine("Доступные команды:");
        Console.WriteLine(" - Run    : Персонаж начинает бежать.");
        Console.WriteLine(" - Attack : Персонаж начинает атаковать.");
        Console.WriteLine(" - Stop   : Персонаж останавливается.");
        Console.WriteLine(" - Exit   : Завершить программу.\n");

        string input;
        do
        {
            // Обновляем текущее состояние
            character.Update();

            // Ввод команды с клавиатуры
            Console.Write("\nВведите команду: ");
            input = Console.ReadLine();

            // Передача команды персонажу
            character.HandleInput(input);

        } while (input != "Exit");

        Console.WriteLine("Симуляция завершена.");
    }
}
