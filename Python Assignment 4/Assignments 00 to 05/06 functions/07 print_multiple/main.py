def print_multiple(message, repeats):
    """Prints the message the specified number of times, each on a new line"""
    for _ in range(repeats):
        print(message)  # Each print automatically adds a newline

def main():
    message = input("Please type a message: ")
    repeats = int(input("Enter a number of times to repeat your message: "))
    print_multiple(message, repeats)

if __name__ == '__main__':
    main()