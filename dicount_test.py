def calculate_discount(price, discount_percent):
  """Calculates the final price after applying a discount.

  Args:
    price: The original price of the item.
    discount_percent: The discount percentage.   


  Returns:
    The final price after applying the discount, or the original price if no discount
    was applied.
  """

  if discount_percent >= 20:
    discount_amount = price * discount_percent / 100
    final_price = price - discount_amount
  else:
    final_price = price

  return final_price   


# Get the original price from the user
original_price = float(input("Enter the original price of the item: "))

# Get the discount percentage from the user
discount_percent = float(input("Enter the discount percentage: "))

# Calculate the final price
final_price = calculate_discount(original_price, discount_percent)   


# Print the final price
print("The final price is:", final_price)
