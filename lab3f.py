#!/usr/bin/env python3

# Place my_list below this comment (before the function definitions)
my_list = [1, 2, 3, 4, 5]

def add_item_to_list(ordered_list):
    # This function appends a new item to the list with the value (last item + 1)
    last_item = ordered_list[-1]  # Get the last item in the list
    ordered_list.append(last_item + 1)  # Append (last item + 1) to the list

def remove_items_from_list(ordered_list, items_to_remove):
    # This function removes all values found in items_to_remove from ordered_list
    ordered_list[:] = [item for item in ordered_list if item not in items_to_remove]

# Main code
if __name__ == '__main__':
    print("Original List:", my_list)
    
    # Add items to the list
    add_item_to_list(my_list)
    add_item_to_list(my_list)
    add_item_to_list(my_list)
    
    print("List after adding items:", my_list)  # [1, 2, 3, 4, 5, 6, 7, 8]
    
    # Remove specified items from the list
    remove_items_from_list(my_list, [1, 5, 6])
    
    print("List after removing items:", my_list)  # [2, 3, 4, 7, 8]
