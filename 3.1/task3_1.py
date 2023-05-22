from collections import defaultdict

first_array = list(map(int, input().split()))
second_array = list(map(int, input().split()))

dictionary = defaultdict(int)
for value in first_array:
    if value not in dictionary.keys():
        dictionary[value] = second_array.count(value)

result = []
for value in first_array:
    result.append(dictionary[value])

print(*result, end=" ")