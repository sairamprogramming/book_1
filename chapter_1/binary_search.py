# This is a simple implementation of binary search.

def binary_search(lst,item):

    low = 0
    high = len(lst) - 1

    while low < high:
        mid = (low + high) // 2

        if lst[mid] < item:
            low = mid + 1
        elif lst[mid] > item:
            high = mid - 1
        else:
            return mid

    return None


def test_unit(lst,item):
    index = binary_search(lst,item)

    if index != None:
        print(lst[index] == item)
        print("The index where element is found at index:",index)
    else:
        print(False)
        print("Element is not present in the given list.")

# Testing for empty list.
# lst = []
# test_unit(lst,1)

# Testing for element present in the list.
# lst = [x for x in range(1,10)]
# print(lst)
# test_unit(lst,5)

# Testing for element not present in the list.
# lst = [x for x in range(1,10)]
# print(lst)
# test_unit(lst,200)
