array = list(map(int, input().split()))
count = int(input())

def bubble_sort(arr):
    for i in range(len(arr) - 1):
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        if i == count - 1:
            print(" ".join(map(lambda x: str(x), arr)))

bubble_sort(array)
print(" ".join(map(lambda x: str(x), array)))
