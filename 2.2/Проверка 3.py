n, m, l = map(int, input().split())
many_legs = [ list(map(int, input().split())) for i in range(n) ]
many_arms = [ list(map(int, input().split())) for i in range(m) ]

def search(leg_array, arm_array):
    min_item = float("inf")
    min_item_ind = 0
    for k in range(len(leg_array)):
        max_btw_arrays = leg_array[k] if leg_array[k] > arm_array[k] else arm_array[k]
        if max_btw_arrays <= min_item:
            min_item = max_btw_arrays
            min_item_ind = k
    return min_item_ind

if __name__ == "__main__":
    for _ in range(int(input())):
        i, j = map(int, input().split())
        print(search(many_legs[i], many_arms[j]), sep="\n")