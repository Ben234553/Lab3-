#!/usr/bin/env python3

# Declare the list "my_list" before any function definitions
my_list = [100, 200, 300, 'six hundred']

def give_list():
    # Does not accept any arguments
    # Returns all of the items in the global object my_list unchanged
    return my_list

def give_first_item():
    # Does not accept any arguments
    # Returns the first item in the global object my_list as a string
    return str(my_list[0])

def give_first_and_last_item():
    # Does not accept any arguments
    # Returns a list that includes the first and last items in the global object my_list
    return [my_list[0], my_list[-1]]

def give_second_and_third_item():
    # Does not accept any arguments
    # Returns a list that includes the second and third items in the global object my_list
    return my_list[1:3]

if __name__ == '__main__':   # This section also referred to as a "main block"
    print(give_list())                      # Output: [100, 200, 300, 'six hundred']
    print(give_first_item())                # Output: '100'
    print(give_first_and_last_item())       # Output: [100, 'six hundred']
    print(give_second_and_third_item())     # Output: [200, 300]
