namespace Builder
{
    public class Window
    {
        public string? Title { get; set; }
        public (int Width, int Height) Size { get; set; }
        public (int X, int Y) Position { get; set; }

        public override string ToString()
        {
            return $"Window: Title = {Title ?? "No Title"}, Size = ({Size.Width}x{Size.Height}), Position = ({Position.X}, {Position.Y})";
        }
    }
}
