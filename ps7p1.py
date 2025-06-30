def calculate_total(quantity, price):
    total = quantity * price
    if total > 10000.00:
        total *= 0.90
    return total
def main():
    grand_total = 0.0
    while True:
        answer = input("Do you want to enter a quantity and price? (Yes or No): ").strip().lower()
        if answer != "yes":
            break
        try:
            quantity = int(input("Enter quantity: "))
            price = float(input("Enter price: $"))
            total = calculate_total(quantity, price)
            grand_total += total
            print(f"\nQuantity: {quantity}")
            print(f"Price per item: ${price:.2f}")
            print(f"Total (with discount if applicable): ${total:.2f}\n")
        except ValueError:
            print("Invalid input. Please enter numeric values for quantity and price.\n")
    print(f"Extended (Grand) Total: ${grand_total:.2f}")
main()
