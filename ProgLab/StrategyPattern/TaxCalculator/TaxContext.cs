namespace TaxCalculator
{
    public class TaxContext
    {
        public ITaxStrategy TaxStrategy { get; set; } // Убрали `required`

        public TaxContext(ITaxStrategy taxStrategy)
        {
            TaxStrategy = taxStrategy;
        }

        public decimal Calculate(decimal income)
        {
            return TaxStrategy.CalculateTax(income);
        }
    }
}
