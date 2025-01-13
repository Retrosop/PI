namespace CarControlApp
{
    public class AccelerateCarCommand : ICommand
    {
        private readonly Car _car;
        private readonly int _speed;

        public AccelerateCarCommand(Car car, int speed)
        {
            _car = car;
            _speed = speed;
        }

        public void Execute()
        {
            _car.Accelerate(_speed);
        }
    }
}
