def main():
    for i in range(10, 20):  # Iterate from 10 to 19
        if is_odd(i):
            print(f"{i} odd")
        else:
            print(f"{i} even")

def is_odd(value: int):
    """Returns True if the value is odd, False otherwise."""
    return value % 2 == 1

if __name__ == '__main__':
    main()