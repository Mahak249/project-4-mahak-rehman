# Ask the user for a starting number
curr_value = int(input("Enter a number: "))

# Double the number and print until >= 100
if curr_value >= 100:
    print("The number is already 100 or greater. No doubling needed.")
else:
    while curr_value < 100:
        curr_value = curr_value * 2
        print(curr_value, end=' ')
    print()  # Add a newline after the loop