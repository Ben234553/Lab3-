#!/usr/bin/env python3
'''Lab 3 Inv 2 function operate '''
# Author ID : 123236218

def operate(number1, number2, operator):
    result = None  # Initialize the result variable
    
    # Conditional logic to handle operations
    if operator == 'add':
        result = int(number1 + number2)
    elif operator == 'subtract':
        result = int(number1 - number2)
    elif operator == 'multiply':
        result = int(number1 * number2)
    elif operator == 'divide':
        result = 'Error: function operator can be "add", "subtract", or "multiply"'
    else:
        result = 'Error: Invalid operator'
    
    return result  # Only one return statement

if __name__ == '__main__':
    print(operate(10, 5, 'add'))       # Output: 15
    print(operate(10, 5, 'subtract'))  # Output: 5
    print(operate(10, 5, 'multiply'))  # Output: 50
    print(operate(10, 5, 'divide'))    # Output: Error: function operator can be "add", "subtract", or "multiply"
    print(operate(10, 5, 'modulus'))   # Output: Error: Invalid operator
