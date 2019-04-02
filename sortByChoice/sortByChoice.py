def findSmallestIndex(arr):
    smallestItem = arr[0]
    smallestIndex = 0

    for i in range(len(arr)):
        if arr[i] < smallestItem:
            smallestItem = arr[i]
            smallestIndex = i

    return smallestIndex

def sortByChoice(arr):
    newArr = []

    for i in range(len(arr)):
        smallest = findSmallestIndex(arr)
        newArr.append(arr.pop(smallest))

    return newArr

arr = [5, 2, 3, 10, 7, 8]

print(findSmallestIndex(arr))
print(sortByChoice(arr))