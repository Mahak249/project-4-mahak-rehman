def get_last_element(lst):
    """Prints the last element of the provided list."""
    if len(lst) > 0:
        
        print(lst[-1])
    else:
        print("The list is empty!")


def get_lst():
    """Prompts the user to enter list elements and returns the resulting list."""
    lst = []
    while True:
        elem = input("Enter an element (or press Enter to stop): ").strip()
        if not elem:
            break
        lst.append(elem)
    return lst


def main():
    lst = get_lst()
    get_last_element(lst)


if __name__ == '__main__':
    main()