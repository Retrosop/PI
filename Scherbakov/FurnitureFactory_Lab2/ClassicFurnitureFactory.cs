public class ClassicFurnitureFactory : IFurnitureFactory
{
    public IFurniture CreateChair()
    {
        return new ClassicChair();
    }

    public IFurniture CreateSofa()
    {
        return new ClassicSofa();
    }
}
