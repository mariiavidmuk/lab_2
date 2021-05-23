from pip._vendor.msgpack.fallback import xrange

global maximum
global maxi

def lis(arr, n):
    global maximum
    global maxi
    if n == 1:
        return 1
    maxEndingHere = 1
    array = []
    for i in xrange(1, n):
        res = lis(arr, i)
        if arr[i - 1] < arr[n - 1] and res + 1 > maxEndingHere:
            maxEndingHere = res + 1
            array.append(arr[i - 1])
    maximum = max(maximum, maxEndingHere)
    try:
        index1 = arr.index(array[len(array) - 1])
        arr1 = arr[index1:]
        for i in range(len(arr1)):
            if arr1[0] < arr1[i]:
                array.append(arr1[i])
        if maxEndingHere == maxi:
            print(array)
    except:
        pass
    return maxEndingHere


def lis1(array):
    global maximum
    global maxi
    n = len(array)
    maximum = 1
    maxi = None
    maxi = lis(array, n)
    lis(array, n)
    return maximum


arr = [34, 23, 56, 2, 78, 90]
n = len(arr)
print("Length of lis is ", lis1(arr))
