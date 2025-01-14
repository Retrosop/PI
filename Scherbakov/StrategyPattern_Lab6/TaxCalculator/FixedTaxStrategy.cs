namespace TaxCalculator
{
    public class FixedTaxStrategy : ITaxStrategy
    {
        private readonly decimal _taxRate;

        public FixedTaxStrategy(decimal taxRate)
        {
            _taxRate = taxRate;
        }

        public decimal CalculateTax(decimal income)
        {
            return income * _taxRate;
        }
    }
}
