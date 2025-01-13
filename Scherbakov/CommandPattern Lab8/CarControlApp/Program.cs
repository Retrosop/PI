using System;

namespace CarControlApp
{
    class Program
    {
        static void Main(string[] args)
        {
            // Создаём автомобиль
            Car car = new Car();

            // Создаём команды
            StartCarCommand startCommand = new StartCarCommand(car);
            StopCarCommand stopCommand = new StopCarCommand(car);
            AccelerateCarCommand accelerateCommand = new AccelerateCarCommand(car, 100);

            // Создаём пульт управления с установленной командой
            RemoteControl remoteControl = new RemoteControl
            {
                Command = startCommand
            };

            // Запускаем автомобиль
            remoteControl.PressButton();

            // Устанавливаем новую команду
            remoteControl.Command = accelerateCommand;
            remoteControl.PressButton();

            // Останавливаем автомобиль
            remoteControl.Command = stopCommand;
            remoteControl.PressButton();
        }
    }
}
