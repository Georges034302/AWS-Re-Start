# Generate a random list from first to last of size n (all STDIN)
# Determine the position of a target element in a list
# Show the position if the element exist, other print a message
# Binary search works if the list is sorted

import random as ran

def random_list(first,last,n):
    return ran.sample(range(first,last),n)

def binary_search(e, numbers):
    first = 0               # first index
    last = len(numbers)-1   # last index
    mid = 0
    
    while first <= last:
        mid = (first+last)// 2  # middle index (// flooring operator)
        if numbers[mid] == e:
            return mid          # target found
        elif numbers[mid] < e:
            first = mid + 1     # discard the entire left-side of the list
        else:
            last = mid - 1      # discard the right side of the list
    return -1   # target does not exist in the list

def search():
    first = int(input("First = "))
    last = int(input("Last = "))
    size = int(input("Size = "))
    mylist = random_list(first,last,size)
    mylist.sort() # sorting the list elements
    print(mylist)
    e = int(input("Target = "))
    pos = binary_search(e,mylist)
    if pos != -1:
        print(f'Target {e} is found at position {pos}')
    else:
        print(f'Target {e} does not exist in the list')
search()
