'''
question1.py

Implementation of the flowchart in question1.png.
'''

def flowchart(input_value):
    
    returnMessage = ""

    if input_value==0:
       returnMessage = "zero"
    elif input_value>0:
        if input_value%2==0:
            returnMessage = "positive-even"
        else:
            returnMessage = "positive-odd"
    elif input_value<0:
        if input_value%2==0:
            returnMessage = "negative-even"
        else:
            returnMessage = "negative-odd"
    else:
        returnMessage = "enter a valod parameter"
    
    return returnMessage

