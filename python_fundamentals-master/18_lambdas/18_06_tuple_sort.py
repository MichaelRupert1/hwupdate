'''
Use a lambda expression to sort a list of tuples based on the number value in the tuple.
For example:

unsorted_list = [('first_element', 4), ('second_element', 2), ('third_element', 6)]
sorted_list = [('second_element', 2), ('first_element', 4), ('third_element', 6)]

'''
def sortt(unsorted_list):
    unsorted_list.sort(key = lambda x:x[1])
    # unsorted_list.sort(key = lambda x:x[0])
    # will sort by name[0] instead number[1]
    return unsorted_list
    

unsorted_list = [('first_element', 4), ('second_element', 2), ('third_element', 6)]
print(sortt(unsorted_list))
