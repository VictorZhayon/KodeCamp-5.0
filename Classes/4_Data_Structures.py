'''
    int, float, str, bool
    
    DATA STRUCTURE
    List, Tuple, Set, Dictionary
    
    There are ways of organizing, storing and managing data efficiently to perform operations effectively
    
    Len() - Returns the number of items in an object
    It works for every data structure in Python, including lists, tuples, sets, and dictionaries.
'''

# List Data Strucure in Python
# List is basically an ordered mutable collection of items, seperated by commas and enclosed in square brackets.
# These items can be of any data type, including other lists.
# Lists are dynamic, meaning they can grow and shrink in size as needed.
# They support duplications, meaning you can have multiple occurrences of the same value in a list.

# Example of a list
ages = [20, 30, 40, 50, 60, 70]
# Lists can contain different data types
mixed_list = [1, "Hello", 3.14, True, [1, 2, 3]]
# Lists are mutable, meaning you can change their content

print("Original List:", ages)
print()
print("Mixed List:", mixed_list)

# Accessing elements in a list
# Syntax: list_name[index]
print("First element in ages:", ages[0])  # Accessing the first element
print("Last element in ages:", ages[-1])  # Accessing the last element
print()

# Changing elements in a list
# Syntax: list_name[index] = new_value

ages[0] = 25  # Changing the first element
print("Updated List:", ages)

item_count = len(ages)  # Getting the number of items in the list
print(item_count)
ages[item_count - 1] = 100  # Changing the last element
print("Updated List after changing last element:", ages)
print()

# To see all the methods available for a list, you can use the dir() function
print("List methods:", dir(ages))
# or list_name.list_method_name()
print()

#List Methods
# .append() adds items to the list, specifically the end.
ages.append(1000)
print(ages)
print()
# .copy() creates a shallow copy of the list.
'''
    There are two types of memory:
    - Heap Memory: Used for storing objects and data structures.
    - Stack Memory: Used for storing function calls and local variables.
'''

final_mult = 1

for item in ages:
    final_mult = item * final_mult
print("Final multiplication of all items in ages:", final_mult)

print()
print()
print()

# Tuple Data Structure in Python
# A tuple is an ordered collection of items, similar to a list, but it is immutable, meaning once created, its content cannot be changed.
# Tuples are defined using parentheses () and can contain items of different data types.
# Example of a tuple
ages_tuple = (20, 30, 40, 50, 60, 70)
# Tuples can also contain different data types
mixed_tuple = (1, "Hello", 3.14, True, (1, 2, 3))
# Tuples are immutable, meaning you cannot change their content after creation
print("Original Tuple:", ages_tuple)
print("Mixed Tuple:", mixed_tuple)
# Accessing elements in a tuple
print("First element in ages_tuple:", ages_tuple[0])  # Accessing the first element
print("Last element in ages_tuple:", ages_tuple[-1])  # Accessing the last element
print()
# Changing elements in a tuple is not allowed, as tuples are immutable
# However, you can create a new tuple with the desired changes
new_ages_tuple = ages_tuple[:2] + (25,) + ages_tuple[3:]  # Changing the third element
print("New Tuple after changing third element:", new_ages_tuple)
# To see all the methods available for a tuple, you can use the dir() function
print("Tuple methods:", dir(ages_tuple))
# or tuple_name.tuple_method_name()
# Tuple Methods
# .count() returns the number of occurrences of a specified value in the tuple.
print("Count of 20 in ages_tuple:", ages_tuple.count(20))
# .index() returns the index of the first occurrence of a specified value in the tuple.
print("Index of 30 in ages_tuple:", ages_tuple.index(30))
# .index() raises a ValueError if the specified value is not found in the tuple.
# .index() can also take a start and end index to search within a specific range.


# Dictionary Data Structure in Python
# A dictionary is an unordered collection of key-value pairs, where each key is unique.
# Dictionaries are defined using curly braces {} and can contain items of different data types.
# Example of a dictionary
ages_dict = {
    "student1": 20,
    "student2": 40,
    "student3": 60,
}

# Acessing elements in a dictionary
# Syntax: dict_name[key]
print("Age of student1:", ages_dict["student1"])  # Accessing the value associated with the key "student1"