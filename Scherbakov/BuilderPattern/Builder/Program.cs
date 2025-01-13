using System;

namespace Builder
{
    class Program
    {
        static void Main(string[] args)
        {
            // Создаём окно с использованием строителя
            var window = new WindowBuilder()
                .SetTitle("My Application")
                .SetSize(800, 600)
                .SetPosition(100, 100)
                .Build();

            Console.WriteLine(window);
        }
    }
}
