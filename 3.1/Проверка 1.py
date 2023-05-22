arrayBase = list(map(int, input().split()))
arraySearch = list(map(int, input().split()))

hashMap = {}
result = []

for digit in arrayBase:
    if digit not in hashMap.keys():
        hashMap[digit] = arraySearch.count(digit)
    result.append(hashMap[digit])

print(*result, end=" ")