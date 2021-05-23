import numpy as np
def create_martix(arr):
    arr2 = arr
    t = len(arr)
    matrix = np.zeros((t, t))
    for i in range(t):
        for j in range(t):
            if arr[i] == arr2[j]:
                matrix[i][j] = 1
            else:
                matrix[i][j] = 0
    return matrix


def repeat_substring(string):
    text = list(string)
    matrix = create_martix(text)
    t = len(matrix)
    diag = [matrix.diagonal(i) for i in range(int((t - 1)), int(0), -1)]
    array = [n.tolist() for n in diag]
    maximum = 0
    diagonal = 0
    for i in range(len(array)):
        ones =0
        for j in range(len(array[i]) - 2):
            if array[i][j+1] == 1 and (array[i][j+2] ==1 or array[i][j] ==1):
                ones += array[i][j+1]
            if array[i][0] == 1 and array[i][1] == 1:
                ones += array[i][0]
            if array[i][len(array[i]) -1] == 1 and array[i][len(array[i]) - 2] == 1:
                ones += len(array[i]) -1
            if ones > maximum:
                maximum = ones
                diagonal = array[i]
    result = text[len(text) - len(diagonal):]
    for i in range(len(diagonal)):
        if diagonal[i] == 1:
            print(result[i], end = '')


repeat_substring('abccdabdd')