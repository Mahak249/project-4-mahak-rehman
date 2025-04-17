def count_numbers():
    numbers = []
    counts = {}
    
    # Get input from user
    print("Enter numbers (one per line, press Enter without input to finish):")
    while True:
        user_input = input("Enter a number: ")
        if user_input == "":
            break
        try:
            num = int(user_input)
            numbers.append(num)
        except ValueError:
            print("Please enter a valid number or press Enter to finish.")
    
    # Count occurrences of each number
    for num in numbers:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1
    
    # Display the results
    for num, count in sorted(counts.items()):
        print(f"{num} appears {count} {'time' if count == 1 else 'times'}.")

# Run the program
count_numbers()