namespace CarControlApp
{
    public class StopCarCommand : ICommand
    {
        private readonly Car _car;

        public StopCarCommand(Car car)
        {
            _car = car;
        }

        public void Execute()
        {
            _car.Stop();
        }
    }
}
