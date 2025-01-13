public class PastaFactory : FoodFactory
{
    public override IFood CreateFood()
    {
        return new Pasta();
    }
}
