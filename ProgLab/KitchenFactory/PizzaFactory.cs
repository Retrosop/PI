public class PizzaFactory : FoodFactory
{
    public override IFood CreateFood()
    {
        return new Pizza();
    }
}
