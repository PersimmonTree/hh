#   Задача 1

#   Для n=5 и k=3 число различных сочетаний из n по k (Cnk) равно 10:
#   (1,2,3), (1,2,4), (1,2,5), (1,3,4), (1,3,5), (1,4,5), (2,3,4), (2,3,5), (2,4,5) и (3,5,4)
#   Для какого количества пар n и k, при условии 1<=n<159 и 1<=k<n, число сочетаний из n по k больше 1000000?

#   При решении используем https://ru.wikipedia.org/wiki/%D0%A1%D0%BE%D1%87%D0%B5%D1%82%D0%B0%D0%BD%D0%B8%D0%B5

import math

def countCombination(n, k):
    if (n > k):
        return math.factorial(n) / (math.factorial(k) * math.factorial(n - k))
    else:
        return 0

result = 0

for n in range(1, 159):
    for k in range(1, n):
        if countCombination(n, k) > 1000000:
            result += 1

print(result)