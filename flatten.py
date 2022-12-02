def flatten(lst):
    flat_list = []
    
    for element in lst:
        if isinstance(element, list):
            flat_list.extend(flatten(element))
        else:
            flat_list.append(element)
    
    return flat_list

my_list = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]

print(flatten(my_list))