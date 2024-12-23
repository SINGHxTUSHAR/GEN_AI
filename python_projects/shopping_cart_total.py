## func() to calculate total items cost in cart
def cart_calculator(cart):
    total = 0
    for item in cart:
        total += item["price"] * item["quantity"]
    return total

## fucn() to add more items to cart
def add_items_to_cart(cart):
    while True:
        print("\nEnter details of the new item:")
        name = input("Name of the item: ")
        try:
            price = float(input("Price of the item (e.g., 1.50): "))
            quantity = int(input("Quantity of the item: "))
        except ValueError:
            print("Invalid input! Please enter a valid price and quantity.")
            continue

        # Add the new item to the cart
        cart.append({'name': name, 'price': price, 'quantity': quantity})
        print(f"Added {quantity} x {name}(s) at ${price:.2f} each to the cart.")

        # Ask the user if they want to add more items
        add_more = input("Do you want to add another item? (yes/no): ").strip().lower()
        if add_more != 'yes':
            break

## func() to remove the item from cart before billing(total)
def remove_items_from_cart(cart):
    while True:
        print("\nCurrent cart:")
        for index, item in enumerate(cart, start=1):
            print(f"{index}. {item['quantity']} x {item['name']}(s) at ${item['price']:.2f} each")

        try:
            item_number = int(input("\nEnter the number of the item to remove (or 0 to stop): "))
        except ValueError:
            print("Invalid input! Please enter a valid number.")
            continue

        if item_number == 0:
            break
        elif 1 <= item_number <= len(cart):
            removed_item = cart.pop(item_number - 1)
            print(f"Removed {removed_item['quantity']} x {removed_item['name']}(s) from the cart.")
        else:
            print("Invalid number! Please select a valid item number.")

## default cart
cart = [
    {"name": "Book", "price": 10, "quantity": 2},
    {"name": "Pen", "price": 5, "quantity": 3},
    {"name": "Notebook", "price": 15, "quantity": 1},
    {"name": "Pencil", "price": 2, "quantity": 5}
]

## showing items in your cart
print("\nYour current cart:")
for item in cart:
    print(f"{item['quantity']} x {item['name']}(s) at ${item['price']:.2f} each")

## add more items in your cart
print("\nDo you want to add any items to your cart?")
add_choice = input("Enter 'yes' to add items or 'no' to proceed: ").strip().lower()
if add_choice == 'yes':
    add_items_to_cart(cart)

## if to remove item before total
print("\nDo you want to remove any items from your cart?")
remove_choice = input("Enter 'yes' to remove items or 'no' to proceed: ").strip().lower()
if remove_choice == 'yes':
    remove_items_from_cart(cart)


total_cost = cart_calculator(cart)
print("Total cost:", total_cost)

