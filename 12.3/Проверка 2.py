def sift_up(ind: int) -> None:
    if ind == 0:
        return
    parent_ind = (ind - 1) // 2
    if heap[parent_ind] > heap[ind]:
        heap[ind], heap[parent_ind] = heap[parent_ind], heap[ind]
        sift_up(parent_ind)

def sift_down(ind: int) -> None:
    left, right = 2 * ind + 1, 2 * ind + 2
    nodeInd = ind
    if left < len(heap) and heap[nodeInd] > heap[left]: nodeInd = left
    if right < len(heap) and heap[nodeInd] > heap[right]: nodeInd = right
    if nodeInd != ind:
        heap[ind], heap[nodeInd] = heap[nodeInd], heap[ind]
        sift_down(nodeInd)

def pop():
    if len(heap) == 1:
        return heap.pop()
    minimum = heap[0]
    heap[0] = heap.pop()
    sift_down(0)
    return minimum

def add(value):
    heap.append(value)
    sift_up(len(heap) - 1)
    return "ok"

def size():
    return len(heap)

if __name__ == "__main__":
    heap = []
    n, last_volume = map(int, input().split())

    for _ in range(n):
        p, v = map(int, input().split())
        add((-(p / v), p, v))

    total_sum = 0
    for _ in range(size()):
        item = pop()
        if last_volume < item[2]:
            total_sum += last_volume * item[0] * -1
            break
        else:
            last_volume -= item[2]
            total_sum += item[1]

    print('{:.2f}'.format(total_sum))