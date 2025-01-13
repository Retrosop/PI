using System;

public class FurnitureClient
{
    private readonly IFurnitureFactory _furnitureFactory;

    public FurnitureClient(IFurnitureFactory furnitureFactory)
    {
        _furnitureFactory = furnitureFactory;
    }

    public void CreateFurniture()
    {
        var chair = _furnitureFactory.CreateChair();
        var sofa = _furnitureFactory.CreateSofa();

        chair.Create();
        sofa.Create();
    }
}
