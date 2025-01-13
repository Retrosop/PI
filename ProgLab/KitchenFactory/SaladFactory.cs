public class SaladFactory : FoodFactory
{
    public override IFood CreateFood()
    {
        return new Salad();
    }
}
