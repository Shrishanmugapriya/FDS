# Sample data
item_prices = [50, 30, 20]        # Price of 3 items
quantities = [2, 1, 3]            # Quantity of each item
discount_rate = 10                # 10% discount
tax_rate = 5                      # 5% tax

# Step 1: Calculate subtotal (price * quantity for each item)
subtotal = sum(p * q for p, q in zip(item_prices, quantities))

# Step 2: Apply discount
discount_amount = (discount_rate / 100) * subtotal
subtotal_after_discount = subtotal - discount_amount

# Step 3: Apply tax
tax_amount = (tax_rate / 100) * subtotal_after_discount
total_cost = subtotal_after_discount + tax_amount

# Output
print("Subtotal: ₹",subtotal)
print(f"Discount (@{discount_rate}%): -₹{discount_amount:.2f}")
print(f"Tax (@{tax_rate}%): +₹{tax_amount:.2f}")
print(f"Total cost to be paid: ₹{total_cost:.2f}")
