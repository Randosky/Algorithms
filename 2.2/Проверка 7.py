import array

# n, m, l = map(int, input().split())
# many_legs = [array.array("i", map(int, input().split())) for _ in range(n)]
# many_arms = [array.array("i", map(int, input().split())) for _ in range(m)]
# q = int(input())

n, m, l = 4, 3, 5
many_legs = [[1, 2, 3, 4, 5], [1, 1, 1, 1, 1], [0, 99999, 99999, 99999, 99999], [0, 0, 0, 0, 99999]]
many_arms = [[5, 4, 3, 2, 1], [99999, 99999, 99999, 0, 0], [99999, 99999, 0, 0, 0]]
q = 2
q_pairs = [[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2], [3, 0], [3, 1], [3, 2]]
# q_pairs = [[2, 1], [2, 2]]

def search(leg_array, arm_array):
    left = 0
    right = l - 1
    min_pair = float("inf")
    min_index = 0
    middle_pair = (left + right) // 2
    if leg_array.count(leg_array[0]) == l:
        return l-1

    while left <= right:
        middle = (left + right) // 2
        m_max = max(leg_array[middle], arm_array[middle])
        if m_max <= min_pair:
            min_pair = m_max
            min_index = middle
        if leg_array[middle] > arm_array[middle]:
            left = middle + 1
        else:
            right = middle - 1

    if max(leg_array[middle_pair], arm_array[middle_pair]) < min_pair:
        return middle_pair
    return min_index

result = []
for i, j in q_pairs:
    result.append(search(many_legs[i], many_arms[j]))
print(*result, sep="\n")