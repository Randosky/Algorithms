k, m, n = map(int, input().split())

def get_permutations(minimum, maximum, result, ind=0, counter=0):
    if ind == k:
        counter += 1
        print(*result)
        return counter

    elementsBefore = 0
    for i in range(minimum , maximum + 1):
        elementsToAppend = k - ind - 1
        if i != result[ind - 1]:
            if elementsBefore >= elementsToAppend:
                result[ind] = i
                counter = get_permutations(minimum, i - 1, result, ind + 1, counter)

            elementsBefore += 1
        else:
            break

    return counter

print(get_permutations(m, n, [0] * k))
