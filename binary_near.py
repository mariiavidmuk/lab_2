


def binary_near(array, x):
    global old
    array = sorted(array)
    n = len(array)
    old = n- 1
    if x < array[0]: return -1
    if x >= array[n - 1]: return n - 1
    if old >= 0 and old < n - 1:
        inc = 1
        left = right = old
        if x < array[old]:
            while 1:
                left -= inc
                print('lf')
                if left <= 0:
                    left = 0
                    break
                if array[left] <= x:
                    break
                r0 = left
                inc <<= 1
        else:
            while 1:
                right += inc
                if right >= n - 1:
                    r0 = n - 1
                    break
                if array[right] > x: break
                l0 = right
                inc <<= 1
    else:
        left = 0
        right = n - 1
        while left < right - 1:
            a = (right + left) >> 1
            if x >= array[a]:
                left = a
            else:
                right = a
        old = left
    return old


array = [0, 2, 4, 6, 7, 10, 11, 14, 15]
print('The value should go after value with index', binary_near(array, 8))
