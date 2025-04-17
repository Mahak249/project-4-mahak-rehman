def find_average(num1, num2):
    """Calculate the average of two numbers."""
    return (num1 + num2) / 2

# Get input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Compute and print the average
average = find_average(num1, num2)
print(f"The average of {num1} and {num2} is: {average}")