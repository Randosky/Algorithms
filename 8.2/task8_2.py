import random


def quickselect(arr, k):
    if len(arr) == 1:
        return arr[0]

    pivot = random.choice(arr)
    left = [x for x in arr if x < pivot]
    right = [x for x in arr if x > pivot]
    equal = [x for x in arr if x == pivot]

    if k < len(left):
        return quickselect(left, k)
    elif k < len(left) + len(equal):
        return equal[0]
    else:
        return quickselect(right, k - len(left) - len(equal))


arr = list(map(int, input().split()))
k = int(input())

result = quickselect(arr, k)

print(result)