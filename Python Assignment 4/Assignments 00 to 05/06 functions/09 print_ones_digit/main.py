def print_ones_digit(num):
    """Prints the ones digit of a number."""
    ones_digit = num % 10
    print(f"The ones digit is {ones_digit}")

def main():
    num = int(input("Enter a number: "))
    print_ones_digit(num)

if __name__ == '__main__':
    main()