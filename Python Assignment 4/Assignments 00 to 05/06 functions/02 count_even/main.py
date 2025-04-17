
def count_even():
    numbers = []
    while True:
        user_input = input("Enter an integer or press enter to stop: ")
        if user_input == "":
            break  # Exit loop on empty input
        try:
            num = int(user_input)
            numbers.append(num)
        except ValueError:
            print("Invalid input. Please enter an integer or press enter to stop.")

    even_count = sum(1 for num in numbers if num % 2 == 0)
    print(f"Number of even numbers: {even_count}")


count_even()