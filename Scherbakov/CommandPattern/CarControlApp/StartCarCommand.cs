namespace CarControlApp
{
    public class StartCarCommand : ICommand
    {
        private readonly Car _car;

        public StartCarCommand(Car car)
        {
            _car = car;
        }

        public void Execute()
        {
            _car.Start();
        }
    }
}
