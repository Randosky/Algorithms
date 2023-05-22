def partition(array, left, right):
    if right - left <= 1:
        return left

    i, j = left, right - 1
    separator = array[right - 1][0]

    while i <= j:
        while array[i][0] < separator:
            i += 1
        while array[j][0] > separator:
            j -= 1

        if i < j:
            array[i], array[j] = array[j], array[i]
            i += 1
            j -= 1
        else:
            break

    return i

def qsort(array, left, right):
    if right - left <= 1:
        return

    while not right - left <= 1:
        middle = partition(array, left, right)
        if middle - left > right - middle:
            qsort(array, middle, right)
            right = middle
        else:
            qsort(array, left, middle)
            left = middle



n = int(input())
bacterias = []
for _ in range(n):
    bacterias.append(tuple(map(int, input().split())))

planets = list(map(int, input().split()))
qsort(bacterias, 0, len(bacterias))

for planet in planets:
    count = 0
    for bacteria in bacterias:
        if bacteria[0] > planet:
            break
        if bacteria[1] >= planet:
            count += 1
    print(count)