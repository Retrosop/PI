namespace TaxCalculator
{
    public class ProgressiveTaxStrategy : ITaxStrategy
    {
        public decimal CalculateTax(decimal income)
        {
            if (income <= 50000)
            {
                return income * 0.1m;
            }
            else if (income <= 100000)
            {
                return income * 0.2m;
            }
            else
            {
                return income * 0.3m;
            }
        }
    }
}
