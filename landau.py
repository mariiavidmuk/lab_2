def landau(text, pattern):  # 2:Нечіткий пошук (близькі за відстанню, алгоритм Ландау-Вішкіна)
    leven = []
    n, m = len(text), len(pattern)
    column = range(m + 1)
    for i in range(1, n + 1):
        prev_column, column = column, [0] * (m + 1)
        for j in range(1, m + 1):
            add, delete, change = prev_column[j] + 1, column[j - 1] + 1, prev_column[j - 1]
            if pattern[j - 1] != text[i - 1]:
                change += 1
            column[j] = min(add, delete, change)
        leven.append(column[m])
    k = leven[len(leven)-1]
    dis = 0
    for i in range(0, n):
        if leven[i] == k:
            print(text[dis:i+1])
            dis = i + 1

a = str(input())
b = str(input())
landau(a, b)