'''
keywords.py

Create functions that use keyword arguments
with default values.
'''

# Create a function called welcome_message():
# if no input argument is provided
# it returns the string 'Hello and welcome'
# if a keyword argument called user_name is provided
# it returns 'Hello, <user_name>, and welcome'
# if a keyword argument called place is provided
# it returns 'Hello and welcome to <place>'
# if both user_name and place are provided
# it returns 'Hello, <user_name>, and welcome to <place>

def welcome_message(user_name = '', place = ''):

    if place == '': 
        if user_name == '':
            return 'Hello and welcome'
        else:
            return 'Hello, ' + user_name + ', and welcome'
    else:
        if user_name == '':
            return 'Hello and welcome to ' + place
        else:
            return 'Hello, ' + user_name + ', and welcome to ' + place
    
    return None  

# Create a function called list_average()
# without using any libraries to do the maths for you 
# (the point of this exercise is to practice interacting 
# with lists)
# the first argument is a list of numbers
# the second optional keyword arguemt is called avg_type
# if nothing for avg_type provided, return the mean of the list
# if avg_type='mode', return the mode of the list 
# (return list of all modes if there is a tie between multiple values)
# if avg_type='mean', return the mean of the list
# if avg_type='median', return the median of this list

def list_average(number_list, avg_type = 'mean'):
    if avg_type == 'mean':
        total = 0
        for x in number_list:
            total = total + x
        if total == 0:
            return 0
        else:
            return total/(len(number_list))
        
    if avg_type == 'mode':
        n = len(number_list) 

        from collections import Counter
  
        data = Counter(number_list) 
        get_mode = dict(data) 
        mode = [k for k, v in get_mode.items() if v == max(list(data.values()))] 
  
        if len(mode) == n: 
            get_mode = "No mode found"
        else: 
            get_mode = "Mode is / are: " + ', '.join(map(str, mode)) 
      
        return get_mode


    if avg_type == 'median':
        number_list.sort

        if len(number_list) != 0:
            if not (len(number_list) % 2):
                halfway = len(number_list)//2
                median  = (number_list[halfway-1] + number_list[halfway])/2
        else:
            halfway = len(number_list)//2
            median  = number_list[halfway-1] 
        
        return median
    
    return None




