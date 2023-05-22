array = list(map(int, input().split()))
if len(array) % 2 == 0:
    half = len(array) // 2 - 1
else:
    half = len(array) // 2

def insert_sort(arr):
    for i in range(1, len(arr)):
        c = arr[i]
        pt = i
        while pt > 0 and c < arr[pt - 1]:
            arr[pt] = arr[pt - 1]
            pt -= 1
        arr[pt] = c
        if i == half:
            print(" ".join(map(lambda x: str(x), arr)))

insert_sort(array)
print(" ".join(map(lambda x: str(x), array)))
