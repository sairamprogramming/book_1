# This selection sort algorithm, sorts a given list of
# numbers from the smallest to the largest.

# Function that finds the smalest number and returns the index
# of that number.
def find_smallest_index(lst):
    smallest = lst[0]
    smallest_index = 0
    for i in range(1,len(lst)):
        if lst[i] < smallest:
            smallest = lst[i]
            smallest_index = i
    return smallest_index

# Selection sort implementation
def selection_sort(lst):
    sorted_list = []
    for i in range(len(lst)):
        smallest_index = find_smallest_index(lst)
        sorted_list.append(lst.pop(smallest_index))
    return sorted_list

# Another implementation of selection sort
def selection_sort_2(lst):
    sorted_list = []
    while lst:
        smallest_index = find_smallest_index(lst)
        sorted_list.append(lst.pop(smallest_index))
    return sorted_list



from random import shuffle,randint

# Simple test of selection sort (with duplicates)
lst = []
for i in range(10):
    lst.append(randint(0,10))

print(selection_sort_2(lst))
