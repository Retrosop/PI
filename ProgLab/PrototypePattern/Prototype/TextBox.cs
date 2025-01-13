namespace Prototype
{
    // Класс для текстового поля
    public class TextBox : UIElement
    {
        public required string Placeholder { get; set; } // Обязательное поле для текста-заполнителя

        // Реализация метода клонирования
        public override UIElement Clone()
        {
            return new TextBox
            {
                Id = this.Id,
                Name = this.Name,
                Placeholder = this.Placeholder
            };
        }

        public override string ToString()
        {
            return base.ToString() + $", Placeholder: {Placeholder}";
        }
    }
}
