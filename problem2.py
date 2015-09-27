#   Задача 2

#   Дано равенство, в котором цифры заменены на буквы:
#   rrsu + sru = rtty
#   Найдите сколько у него решений, если различным буквам соответствуют различные цифры.

counter = 0
for r in range(1, 10):
    for s in range(1, 10):
        for u in range(0, 10):
            for t in range(0, 10):
                for y in range(0, 10):
                    if (r != s and r != u and r != t and r != y and s != u and s != t and s != y and u != t and u != y and t != y):
                        if int(str(r) + str(r) + str(s) + str(u)) + int(str(s) + str(r) + str(u)) == int(str(r) + str(t) + str(t) + str(y)):
                            print(str(r) + str(r) + str(s) + str(u) + " + " + str(s) + str(r) + str(u) + " = " + str(r) + str(t) + str(t) + str(y))
                            counter += 1

print("counter = " + str(counter))