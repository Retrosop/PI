using SingletonPattern;
using Xunit;

namespace Singleton.Tests
{
    public class LoggerTests
    {
        [Fact]
        public void Logger_ShouldReturnSameInstance()
        {
            // Act
            var instance1 = Logger.GetInstance();
            var instance2 = Logger.GetInstance();

            // Assert
            Assert.Same(instance1, instance2);
        }

        [Fact]
        public void Logger_ShouldLogMessage()
        {
            // Arrange
            var logger = Logger.GetInstance();

            // Act
            logger.Log("Test message");

            // Assert
            // Здесь можно проверить вывод в консоль, если переопределить Console.Out.
            // Например, перехватывая поток вывода (необязательно).
        }
    }
}
