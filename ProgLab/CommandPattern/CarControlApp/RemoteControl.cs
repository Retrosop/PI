namespace CarControlApp
{
    public class RemoteControl
    {
        public required ICommand Command { get; set; }

        public void PressButton()
        {
            Command.Execute();
        }
    }
}
