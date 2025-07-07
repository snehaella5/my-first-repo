print("Hello, World!")

menu = {
    'Paneer Butter Masala': 150,
    'Chicken Biryani': 200,
    'Veg Thali': 120,
    'Tandoori Roti': 10,
    'Gulab Jamun': 40
}

order_history = []

print("\n Welcome to Python Hotel!")
print("Here's our delicious menu:\n")
for item, price in menu.items():
    print(f"{item:25} {price}")

while True:
    order = input("\n Enter an item to order (or type 'done' to finish): ").strip()
    
    if order.lower() == 'done':
        break
    elif order in menu:
        try:
            quantity = int(input(f"How many plates of {order}? "))
            if quantity <= 0:
                print(" Quantity should be a positive number.")
                continue
            cost = menu[order] * quantity
            order_history.append((order, quantity, cost))
            print(f" Added {quantity} x {order} = {cost}")
        except ValueError:
            print(" Please enter a valid number.")
    else:
        print("Sorry, that item is not on the menu.")

# Final Bill Summary
print("\n Your Bill Receipt")
print("-" * 35)
total = 0
for item, qty, price in order_history:
    print(f"{item:20} x{qty:<3} {price}")
    total += price
print("-" * 35)
print(f"{'Total':24} {total}")
print("\nThank you for dining with us!")
