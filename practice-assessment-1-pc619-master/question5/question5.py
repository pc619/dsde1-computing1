'''
question5.py

Simple functions performing operations on basic Python data structures.
'''

# Lists

# Write a function that merges two lists together only if the length of both
# lists is greater than 4. Otherwise return an empty list.
def merge_list(list1, list2):
    joinedList = []
    if (len(list1)>4)&(len(list2)>4):
        joinedList = list1 + list2

    return joinedList

# Write a function that returns a list containing unique values from the input_list.
# In other words, any repeated values are removed.
def unique_values(input_list):
    
    new = []

    for x in input_list:
        if x not in new:
            new.append(x)
    

    return new

# Strings

# Write a function that returns a string where first "x" characters are lower
# case. "x" is passed as the second parameter. 
def start_to_lower(string, x):

    firstx_of_string = string[0:x]

    i = x+1

    rest_of_string = string[-i:]

    string = firstx_of_string.lower() + rest_of_string

    return string

# Write a function that returns the character which first occurs for the second
# time in the string. For example in string "abcdefcab" the character "c"
# occurs twice first. If no character occurs more than once, an empty string
# should be returned. 
def first_double_char(string):

    returnString = ""

    for index in range(len(string)):
        for comparing_index in range(index+1, len(string)):
            if string[index]==string[comparing_index]:
                returnString = string[index]
                break

    return returnString

# Dictionaries

# Write function that returns a sum of all values stored in the dictionary.
def sum_of_dict(dictionary):

    sum_of_dictionary = 0
    for x in dictionary.values():
        sum_of_dictionary = sum_of_dictionary + x

    return sum_of_dictionary

# Write a function that returns a new dictionary where each value is multiplied
# by 3. Example: for input dictionary {'a': 1, 'b': 2, 'c': 3} the returned
# dictionary will be {'a': 3, 'b': 6, 'c': 9}

def multiply_dict(dictionary):

    for x in dictionary:
        dictionary[x]=dictionary[x]*3

    return dictionary

# Arguments


# Write a function with the first argument mandatory and the second optional.
# The first argument accepts a list as an argument, the second accepts two
# strings "max" or "min". The function returns either the maximum or the
# minimum value from the list. The default operation is "max". If the operation
# is neither "max" nor "min" the function should return "None" (the value, not
# the string).
def max_min(input_list, operation):
    return

