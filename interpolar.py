
def interpolar(array, inf, sup, number):
    if (inf <= sup and number >= array[inf] and number <= array[sup]):
        pos = inf + ((sup - inf) // (array[sup] - array[inf]) * (number - array[inf]))
        if array[pos] == number:
            return pos
        if array[pos] < number:
            return interpolar(array, pos + 1, sup, number)
        if array[pos] > number:
            return interpolar(array, inf,pos - 1, number)
    return -1

arr = [0, 2, 4, 6, 7, 10, 11, 14, 15]
n = len(arr)
x = 4
index = interpolar(arr, 0, n - 1, x)
print('The index of element is', index)
