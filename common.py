import numpy as np
global maximum

def common(a, b):
    n = 0
    i = 0
    j = 0
    st1 = list(a)
    st2 = list(b)
    text1 = sorted(st1)  # reverse=True
    text2 = sorted(st2)
    print(text1)
    print(text2)
    size1 = len(st1) - 1
    size2 = len(st2) - 1
    while i < size1 or j < size2:
        if text1[i] < text2[j]:
            i += 1
        elif text1[i] > text2[j]:
            j += 1
        elif text1[i] == text2[j]:
            print(text1[i], end = ' ')
            i += 1
            j += 1
            n += 1
    print()
    return n


print('Amount of common elements = ' + str(common("sdgsdsmbk", "dshjsdal")))