def distance(text1, text2):
   n, m = len(text1), len(text2)
   if n > m:
      text1, text2 = text2, text1
      n, m = m, n
   column = range(n+1)
   for i in range(1, m+1):
      previous_column, column = column, [i]+[0]*n
      for j in range(1,n+1):
         a, b, c = previous_column[j]+1, column[j-1]+1, previous_column[j-1]
         if text1[j-1] != text2[i-1]:
            c += 1
         column[j] = min(a, b, c)

   return column[n]

a = str(input())
b = str(input())
print('Amount of differences:')
print(distance(a, b))

