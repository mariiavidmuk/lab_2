
def binary_search(array, infi, supr, x):
    if supr >= infi:
        middle = (supr + infi) // 2
        if array[middle] == x:
            return middle
        elif array[middle] > x:
            return binary_search(array, infi, middle - 1, x)
        else:
            return binary_search(array, middle + 1, supr, x)


arr = [6, 54, 34, 78, 1, 4, 80]
arr.sort()
search = 78
result = binary_search(arr, 0, len(arr) - 1, search)
print('The index of element is', result)