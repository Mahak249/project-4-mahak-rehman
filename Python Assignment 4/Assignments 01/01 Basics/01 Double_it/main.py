def main():
    # Get initial number from user
    curr_value = int(input("Enter a number: "))
    
    # Double the number until it reaches 100 or more
    while curr_value < 100:
        curr_value = curr_value * 2
        print(curr_value, end=' ')
    
    print()  # Add a newline at the end

if __name__ == "__main__":
    main()