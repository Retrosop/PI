using System;

namespace Prototype
{
    class Program
    {
        static void Main(string[] args)
        {
            // Создаём оригинальные элементы
            Button originalButton = new Button
            {
                Name = "SubmitButton",
                Color = "Blue"
            };

            TextBox originalTextBox = new TextBox
            {
                Name = "UsernameField",
                Placeholder = "Enter your username"
            };

            // Клонируем элементы
            Button clonedButton = (Button)originalButton.Clone();
            TextBox clonedTextBox = (TextBox)originalTextBox.Clone();

            // Изменяем свойства клонированных элементов
            clonedButton.Color = "Red";
            clonedTextBox.Placeholder = "Enter your password";

            // Выводим данные
            Console.WriteLine("Original Button: " + originalButton);
            Console.WriteLine("Cloned Button: " + clonedButton);
            Console.WriteLine("Original TextBox: " + originalTextBox);
            Console.WriteLine("Cloned TextBox: " + clonedTextBox);
        }
    }
}
