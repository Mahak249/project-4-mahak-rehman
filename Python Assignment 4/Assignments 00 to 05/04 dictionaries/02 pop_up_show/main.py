def display_welcome():
    """Display the welcome message and fruit options"""
    print("\n" + "=" * 50)
    print("||" + " " * 46 + "||")
    print("||           FRUIT SHOP CALCULATOR           ||")
    print("||" + " " * 46 + "||")
    print("=" * 50)
    print("\nWelcome to our Fruit Shop!")
    print("Here are our available fruits and prices:\n")
    
def display_fruits(fruits):
    """Display the available fruits and their prices"""
    for fruit, price in fruits.items():
        print(f"- {fruit.capitalize():<10} ${price:.2f} each")
    print("\n" + "-" * 50 + "\n")

def calculate_total(fruits):
    """Calculate the total cost based on user input"""
    total = 0.0
    
    for fruit in fruits:
        while True:
            try:
                quantity = input(f"How many ({fruit}) do you want?: ").strip()
                if not quantity:
                    quantity = 0
                quantity = int(quantity)
                if quantity < 0:
                    print("Please enter a positive number or 0.")
                    continue
                total += quantity * fruits[fruit]
                break
            except ValueError:
                print("Please enter a valid number.")
    
    return total

def display_receipt(total):
    """Display the final receipt"""
    print("\n" + "=" * 50)
    print("\nCalculating your total...\n")
    print(f"Your total is ${total:.2f}")
    print("\n" + "=" * 50)
    print("\nThank you for shopping with us!")
    print("Please come again!\n")
    print("=" * 50)

def main():
    # Dictionary of fruits and their prices
    fruits = {
        'apple': 1.5,
        'durian': 15.0,
        'jackfruit': 10.0,
        'kiwi': 2.5,
        'rambutan': 5.0,
        'mango': 3.0
    }
    
    display_welcome()
    display_fruits(fruits)
    total = calculate_total(fruits)
    display_receipt(total)

if __name__ == '__main__':
    main()