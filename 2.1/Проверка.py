from collections import defaultdict
orks_heights = list(map(int, input().split()))


dictionary = defaultdict(list)
for i, j in enumerate(orks_heights):
    dictionary[j].append(orks_heights.index(j, i))

# dictionary = {}
# for i, j in enumerate(orks_heights):
#     if j in dictionary.keys():
#         dictionary[j].append(orks_heights.index(j, i))
#     else:
#         dictionary[j] = [i]

def searchPosition(height):
    max_count = 0
    for i in range(len(dictionary[height])):
        all_count_right = len(orks_heights) - dictionary[height][i] + 1
        count_equals_right = len(dictionary[height]) - i + 1

        count_equals_left = i + 1
        count_not_equals_right = all_count_right - count_equals_right
        current_max = count_equals_left * count_not_equals_right

        if current_max > max_count:
            max_count = current_max
    return max_count

for h in map(int, input().split()):
    print(searchPosition(h), end=" ")