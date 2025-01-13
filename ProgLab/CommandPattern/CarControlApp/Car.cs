using System;

namespace CarControlApp
{
    public class Car
    {
        public void Start()
        {
            Console.WriteLine("Car started.");
        }

        public void Stop()
        {
            Console.WriteLine("Car stopped.");
        }

        public void Accelerate(int speed)
        {
            Console.WriteLine($"Car is accelerating to {speed} km/h.");
        }
    }
}
