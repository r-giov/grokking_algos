
"""
define a function binary search with parameters array and item. 
assign low to zero, high is the length of the array -9 because we start from 0
"""
def binary_search(arr, item):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]

        if guess == item:
            return mid
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1
    
    return None

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(binary_search(my_list, 9))
print(binary_search(my_list, 8))