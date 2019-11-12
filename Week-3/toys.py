'''
toys.py

Simple toy functions to get comfortable working 
with functions.
'''


# write a function that adds 1
# to the input and prints the result
def inc(a):
    ''' Adds one to the integer a and prints the value'''
    a = a + 1
    print(a)


# write a function that adds 1
# to the input and returns the result
def inc_return(a):
    ''' Adds one to the integer a and returns the value'''
    a = a + 1
    return(a)


# write a function that adds
# the two input numbers together
# and returns the sum
def sum(a, b):
    '''Adds the integers a and b together and returns the value'''
    return(a + b)


# write a function that takes two
# numbers, adds them together using 
# sum() and then increments the sum
# using inc_return
def sum_inc(a, b):
    '''Adds the integers a and b together and adds the value by one'''
    # First the value a and b are added using the sum function.
    # Then the value is added by 1 using the inc_return function.
    return inc_return(sum(a, b))


# write a function that returns a 
# boolean (True or False) for whether 
# the input number is even
def is_even(a_int):
    '''Adds the integers a and b together and adds the value by one'''
    if not (a_int % 2):
          return_boolean = True
    else:
        return_boolean = False
    return return_boolean


# create for loop that takes a string
# and an integer and returns a new string 
# that is the string repeated equal to 
# integer
# e.g. string_repeat('ho', 3) returns
# 'hohoho'
def string_repeat(phrase, repeat):
    '''Takes a string and repeats it as many times as inputted'''

    # Create loop that iterates 'repeat' number of times
    phrase_repeated = ''

    for count in range(0,repeat):
        # Adds the string phrase to phrase_repeated and adds 1 to count.
        phrase_repeated = phrase_repeated + phrase
        count = count + 1

    return phrase_repeated

