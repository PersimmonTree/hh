#   Задача 3

#   Рассмотрим спираль, в которой, начиная с 1 в центре, последовательно расставим числа по часовой стрелке,
#   пока не получится спираль 5 на 5

#   21 22 23 24 25
#   20  7  8  9 10
#   19  6  1  2 11
#   18  5  4  3 12
#   17 16 15 14 13

#   Можно проверить, что сумма всех чисел на диагоналях равна 101.
#   Чему будет равна сумма чисел на диагоналях, для спирали размером 1195 на 1195?

#   При решении используем http://www.mathblog.dk/project-euler-28-sum-diagonals-spiral/

def diagSumByRingNum(ringNumber):
    if ringNumber > 0:
        return 4 * (2 * ringNumber + 1) ** 2 - 12 * ringNumber + diagSumByRingNum(ringNumber - 1)
    else:
        return 1

def diagSum(size):
    if size % 2 == 0:
        raise
    else:
        ringNumber = size // 2
        return diagSumByRingNum(ringNumber)

print("diagSum(3) = " + str(diagSum(3)) + "    " + "diagSumByRingNum(1) = " + str(diagSumByRingNum(1)))

print("diagSum(5) = " + str(diagSum(5)) + "    " + "diagSumByRingNum(2) = " + str(diagSumByRingNum(2)))

print("diagSum(7) = " + str(diagSum(7)) + "    " + "diagSumByRingNum(3) = " + str(diagSumByRingNum(3)))

print("diagSum(1095) = " + str(diagSum(1095)) + "    " + "diagSumByRingNum(547) = " + str(diagSumByRingNum(547)))