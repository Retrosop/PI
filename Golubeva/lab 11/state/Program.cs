using System;

public interface IMusicPlayerState
{
    void Play(MusicPlayer player);
    void Pause(MusicPlayer player);
    void Stop(MusicPlayer player);
}

public class StoppedState : IMusicPlayerState
{
    public void Play(MusicPlayer player)
    {
        Console.WriteLine("Музыка начинает воспроизводиться.");
        player.SetState(new PlayingState());
    }

    public void Pause(MusicPlayer player)
    {
        Console.WriteLine("Музыка уже остановлена.");
    }

    public void Stop(MusicPlayer player)
    {
        Console.WriteLine("Музыка уже остановлена.");
    }
}

public class PlayingState : IMusicPlayerState
{
    public void Play(MusicPlayer player)
    {
        Console.WriteLine("Музыка уже воспроизводится.");
    }

    public void Pause(MusicPlayer player)
    {
        Console.WriteLine("Музыка приостановлена.");
        player.SetState(new PausedState());
    }

    public void Stop(MusicPlayer player)
    {
        Console.WriteLine("Музыка остановлена.");
        player.SetState(new StoppedState());
    }
}

public class PausedState : IMusicPlayerState
{
    public void Play(MusicPlayer player)
    {
        Console.WriteLine("Музыка продолжает воспроизводиться.");
        player.SetState(new PlayingState());
    }

    public void Pause(MusicPlayer player)
    {
        Console.WriteLine("Музыка уже приостановлена.");
    }

    public void Stop(MusicPlayer player)
    {
        Console.WriteLine("Музыка остановлена.");
        player.SetState(new StoppedState());
    }
}

public class MusicPlayer
{
    private IMusicPlayerState _state;

    public MusicPlayer()
    {
        _state = new StoppedState(); // Начальное состояние
    }

    public void SetState(IMusicPlayerState state)
    {
        _state = state;
    }

    public void Play()
    {
        _state.Play(this);
    }

    public void Pause()
    {
        _state.Pause(this);
    }

    public void Stop()
    {
        _state.Stop(this);
    }
}

// Пример использования
class Program
{
    static void Main(string[] args)
    {
        MusicPlayer player = new MusicPlayer();

        player.Play();  // Начинаем воспроизведение
        player.Pause(); // Приостанавливаем
        player.Play();  // Продолжаем воспроизведение
        player.Stop();  // Останавливаем
    }
}
