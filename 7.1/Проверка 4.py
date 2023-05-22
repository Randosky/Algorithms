def get_stones(lst):
    if len(lst) <= 1:
        return 0

    l = lst[:len(lst) // 2]
    r = lst[len(lst) // 2:]
    count = get_stones(l) + get_stones(r)
    count = merge(l, r, count)
    return count

def merge(l, r, count):
    p1, p2 = 0, 0
    while p1 < len(l) and p2 < len(r):
        if l[p1] < r[p2]:
            p1 += 1
        else:
            count += len(l) - p1
            p2 += 1
    return count

if __name__ == "__main__":
    stones = []
    for i in range(int(input())):
        stones.append(int(input()))
    print(get_stones(stones))
