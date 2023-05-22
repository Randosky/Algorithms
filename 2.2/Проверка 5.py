import array

n, m, l = map(int, input().split())
legMonsters = [array.array("i", map(int, input().split())) for _ in range(n)]
handMonsters = [array.array("i", map(int, input().split())) for _ in range(m)]

def findEquals(index_of_min, minimal_in_arrays, legs_by_q_i, hands_by_q_j):
    while index_of_min+1 < l:
        if minimal_in_arrays == max(legs_by_q_i[index_of_min+1], hands_by_q_j[index_of_min+1]):
            minimal_in_arrays = max(legs_by_q_i[index_of_min+1], hands_by_q_j[index_of_min+1])
            index_of_min = index_of_min+1
        else:
            break
    return index_of_min

def binarySearch(legs_by_q_i, hands_by_q_j):
    left = 0
    right = l - 1
    minimal_in_arrays = float("inf")
    index_of_min = 0

    while left <= right:
        middle = (left + right) // 2
        max_pair_middle = max(legs_by_q_i[middle], hands_by_q_j[middle])
        if max_pair_middle <= minimal_in_arrays:
            minimal_in_arrays = max_pair_middle
            index_of_min = middle

        if legs_by_q_i[middle] > hands_by_q_j[middle]:
            right = middle - 1
        elif legs_by_q_i[middle] == hands_by_q_j[middle]:
            break
        else:
            left = middle + 1

    return findEquals(index_of_min, minimal_in_arrays, legs_by_q_i, hands_by_q_j)

answer = []
for _ in range(int(input())):
    i, j = map(int, input().split())
    answer.append(binarySearch(legMonsters[i], handMonsters[j]))
print(*answer, sep=" ")