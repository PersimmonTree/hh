#   Задача 4

#   Число 125874 и результат умножения его на 2 — 251748 можно получить друг из друга перестановкой цифр.

#   Найдите наименьшее положительное натуральное x такое,
#   что числа 2 * x, 6 * x можно получить друг из друга перестановкой цифр.

import itertools

x = 0

while True:

    x += 1

    perm1 = itertools.permutations(str(2 * x), len(str(2 * x)))
    list1 = []
    for p in perm1:
        list1.append(''.join(p))

    perm2 = itertools.permutations(str(6 * x), len(str(6 * x)))
    list2 = []
    for p in perm2:
        list2.append(''.join(p))

    try:
        for s1 in list1:
            for s2 in list2:
                if s1 == s2 and s1[0] != 0:
                    raise StopIteration
    except StopIteration:
        print(" x = " + str(x))
        print("2x = " + str(2 * x))
        print("6x = " + str(6 * x))
        print(s1 + " = " + s2)
        break