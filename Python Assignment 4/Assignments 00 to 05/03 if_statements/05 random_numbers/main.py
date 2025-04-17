import random

N_NUMBERS: int = 10
MIN_VALUE: int = 1
MAX_VALUE: int = 100

def main():
    # Generate N_NUMBERS random integers within the specified range
    numbers = [random.randint(MIN_VALUE, MAX_VALUE) for _ in range(N_NUMBERS)]
    
    # Display results
    print(f"Generated {N_NUMBERS} random numbers between {MIN_VALUE} and {MAX_VALUE}:")
    print(numbers)
    
    # Calculate and show statistics
    print("\nStatistics:")
    print(f"Sum: {sum(numbers)}")
    print(f"Average: {sum(numbers)/len(numbers):.2f}")
    print(f"Maximum: {max(numbers)}")
    print(f"Minimum: {min(numbers)}")

if __name__ == '__main__':
    main()