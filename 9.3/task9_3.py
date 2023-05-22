def makeTower(arr):
    queue = []
    total_w = 0
    count = 0
    for item in arr:
        if item[2] >= total_w:
            count += 1
            total_w += item[3]
            queue.append(item)
            queue.sort(key=lambda x: x[3])
        else:
            if queue[len(queue) - 1][3] > item[3]:
                total_w -= queue.pop()[3]
                queue.append(item)
                queue.sort(key=lambda x: x[3])
                total_w += item[3]

    return count

n = int(input())
gym = []

for _ in range(n):
    params = input().split(";")
    name, hold, weight = params[0], int(params[1]), int(params[2])
    gym.append((hold + weight, name, hold, weight))

gym.sort()
print(makeTower(gym))
