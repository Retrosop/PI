namespace Prototype
{
    // Класс для кнопки
    public class Button : UIElement
    {
        public required string Color { get; set; } // Обязательное поле для цвета

        // Реализация метода клонирования
        public override UIElement Clone()
        {
            return new Button
            {
                Id = this.Id,
                Name = this.Name,
                Color = this.Color
            };
        }

        public override string ToString()
        {
            return base.ToString() + $", Color: {Color}";
        }
    }
}
