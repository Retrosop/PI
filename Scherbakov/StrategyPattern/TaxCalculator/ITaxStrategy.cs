namespace TaxCalculator
{
    public interface ITaxStrategy
    {
        decimal CalculateTax(decimal income);
    }
}
