import math

n, m = map(int, input().split())
plates = list(input().split())
result = [n]


def findPlates():
    for ind in range(1, n // 2 + 1):
        ind_2 = 0
        c = 0

        while ind_2 < ind:
            left_item = plates[ind - ind_2 - 1]
            right_item = plates[ind + ind_2]
            ind_2 += 1
            if left_item == right_item:
                c += 1
            else:
                break

        if c == ind_2:
            result.append(len(plates) - c)


findPlates()
print(*result)
