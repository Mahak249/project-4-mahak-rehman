def main():
    lst = []  

    val = input("Enter a value: ")  
    while val:  # While the user input isn't an empty value
        lst.append(val) # Add val to list
        val = input("Enter a value: ")  # Get the next value to add

    print("Here's the list:", lst)




if __name__ == '__main__':
    main()