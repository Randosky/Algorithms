n, m, l = map(int, input().split())
many_legs = [ list(map(int, input().split())) for i in range(n) ]
many_arms = [ list(map(int, input().split())) for i in range(m) ]

def search(leg_array, arm_array):
    min_item = float('inf')
    min_item_ind = 0
    for i, (leg, arm) in enumerate(zip(leg_array, arm_array)):
        max_btw_arrays = max(leg, arm)
        if max_btw_arrays <= min_item:
            min_item = max_btw_arrays
            min_item_ind = i
    return min_item_ind

for pair in range(int(input())):
    i, j = map(int, input().split())
    print(search(many_legs[i], many_arms[j]))