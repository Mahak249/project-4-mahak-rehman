# Define the list first
fruit_lst = ["apple", "banana", "cherry" , "PineApple"]  # Example list

# Print the length of the list.
lst_length = len(fruit_lst)
print("Length of the list:", lst_length)  # Output: 3

# Add 'mango' at the end of the list. 
fruit_lst.append('mango')

# Print the updated list.
print("Updated list:")
for fruit in fruit_lst:
    print(fruit)