namespace Builder
{
    public class WindowBuilder
    {
        private readonly Window _window;

        public WindowBuilder()
        {
            _window = new Window();
        }

        public WindowBuilder SetTitle(string title)
        {
            _window.Title = title;
            return this;
        }

        public WindowBuilder SetSize(int width, int height)
        {
            _window.Size = (width, height);
            return this;
        }

        public WindowBuilder SetPosition(int x, int y)
        {
            _window.Position = (x, y);
            return this;
        }

        public Window Build()
        {
            return _window;
        }
    }
}
