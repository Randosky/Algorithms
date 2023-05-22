n, m, l = map(int, input().split())
many_legs = [list(map(int, input().split())) for _ in range(n)]
many_arms = [list(map(int, input().split())) for _ in range(m)]
q = int(input())

def search(leg_array, arm_array):
    left, right = 0, l - 1
    min_pair, min_index = 999999999999999999999, 0

    while left <= right:
        middle = (left + right) // 2
        m_max = max(leg_array[middle], arm_array[middle])
        if m_max <= min_pair:
            min_pair = m_max
            min_index = middle

        if leg_array[middle] > arm_array[middle]:
            right = middle - 1
        elif leg_array[middle] < arm_array[middle]:
            left = middle + 1
        else:
            break

    for i in range(min_index+1, l):
        if min_pair == max(leg_array[i], arm_array[i]):
            min_pair = max(leg_array[i], arm_array[i])
            min_index = i
        else:
            break

    return min_index

result = []
for _ in range(q):
    i, j = map(int, input().split())
    result.append(search(many_legs[i], many_arms[j]))
print(*result, sep="\n")