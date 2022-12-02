# This is my flatten function that flattens the list.
def flatten(lst): 
    flat_list = []  # This is the list that will be returned. 
    for element in lst:  # This for loop iterates through the list.
        if isinstance(element, list):  # If the element is a list, it will be flattened.
            flat_list.extend(flatten(element))  # This will flatten the list.
        else:  # If the element is not a list, it will be appended to the flat_list.
            flat_list.append(element)  
    
    return flat_list  # This returns the flattened list.


# This is my reverser function that reverses the list.
def reverser(lst):
    reversed_list = lst[::-1]  # This reverses the list.
    for sub_list in reversed_list:  # This for loop iterates through the reversed list.
        if type(sub_list) == list:  # If the element is a list, it will be reversed.
            sub_list = reverser(sub_list)  
    return reversed_list  # This returns the reversed list.


# This is my list as input. It contains integers, strings, and lists.
my_list = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]

# This is the flattened list.
print(flatten(my_list))

# This is the reversed list.
print(reverser(my_list))