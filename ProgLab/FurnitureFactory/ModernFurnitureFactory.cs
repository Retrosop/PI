public class ModernFurnitureFactory : IFurnitureFactory
{
    public IFurniture CreateChair()
    {
        return new ModernChair();
    }

    public IFurniture CreateSofa()
    {
        return new ModernSofa();
    }
}
