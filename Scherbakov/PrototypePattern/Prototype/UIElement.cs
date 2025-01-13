using System;

namespace Prototype
{
    // Базовый класс для UI элементов
    public abstract class UIElement
    {
        public string Id { get; set; } = Guid.NewGuid().ToString(); // Уникальный ID
        public required string Name { get; set; } // Обязательное имя

        // Абстрактный метод для клонирования
        public abstract UIElement Clone();

        public override string ToString()
        {
            return $"ID: {Id}, Name: {Name}";
        }
    }
}
