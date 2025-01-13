using System;
using System.Collections;
using System.Collections.Generic;

namespace OrderManagementApp
{
    public class OrderCollection : IEnumerable<Order>
    {
        private readonly List<Order> _orders = new();

        public void AddOrder(Order order)
        {
            _orders.Add(order);
        }

        public IEnumerator<Order> GetEnumerator()
        {
            return _orders.GetEnumerator();
        }

        IEnumerator IEnumerable.GetEnumerator()
        {
            return GetEnumerator();
        }

        // Итератор для фильтрации заказов по сумме
        public IEnumerable<Order> GetOrdersAboveAmount(decimal amount)
        {
            foreach (var order in _orders)
            {
                if (order.TotalAmount > amount)
                {
                    yield return order;
                }
            }
        }
    }
}
