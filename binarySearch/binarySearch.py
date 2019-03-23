import math
def binarySearch(item, array):
    min = 0
    max = len(array) - 1

    while min <= max:
        mid = (min + max) / 2
        mid = math.floor(mid)
        value = array[mid]


        if item == value:
            return mid

        if item > value:
            min = mid + 1
        else:
            max = mid - 1

    return None

arr = [1, 3, 5, 6, 7,  10]

print(binarySearch(5, arr))