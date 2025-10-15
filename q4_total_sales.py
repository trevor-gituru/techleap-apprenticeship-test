def calculate_total_sales(sales_data):
  """
  Calculates the total sales from a list of sales data.

  Args:
    sales_data: A list of dictionaries, where each dictionary represents an item
                with "price" and "quantity".

  Returns:
    The total sales amount.
  """
  total = 0
  for item in sales_data:
    total += item.get("price", 0) * item.get("quantity", 0)
  return total

if __name__ == "__main__":
  sales = [
    {"item": "Pen", "price": 20, "quantity": 3},
    {"item": "Book", "price": 200, "quantity": 2},
    {"item": "Bag", "price": 800, "quantity": 1}
  ]
  total_sales = calculate_total_sales(sales)
  print(f"Total sales: {total_sales}")
