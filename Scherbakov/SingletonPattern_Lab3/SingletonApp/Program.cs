using System;
using SingletonPattern;

namespace SingletonApp
{
    class Program
    {
        static void Main(string[] args)
        {
            Logger logger1 = Logger.GetInstance();
            Logger logger2 = Logger.GetInstance();

            if (logger1 == logger2)
            {
                Console.WriteLine("Logger is a singleton. Both instances are the same.");
            }

            logger1.Log("First log message");
            logger2.Log("Second log message");
        }
    }
}
