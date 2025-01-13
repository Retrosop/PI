namespace OrderManagementApp
{
    public class Order
    {
        public int OrderId { get; set; }
        public string CustomerName { get; set; }
        public decimal TotalAmount { get; set; }

        public Order(int orderId, string customerName, decimal totalAmount)
        {
            OrderId = orderId;
            CustomerName = customerName;
            TotalAmount = totalAmount;
        }

        public override string ToString()
        {
            return $"Order ID: {OrderId}, Customer: {CustomerName}, Total Amount: {TotalAmount:C}";
        }
    }
}
