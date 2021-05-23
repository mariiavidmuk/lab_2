
def subsequence(text, pattern):
    index = []
    i = 0
    j = 0
    while (i < len(text)) and (j < len(pattern)):
        if text[i] == pattern[j]:
            index.append(i)
            i += 1
            j += 1
        else:
            i += 1
    print(index)
    return index

a = str(input())
b = str(input())
subsequence(a, b)