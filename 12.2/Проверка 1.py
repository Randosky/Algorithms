def sift_up(ind: int) -> None:
    if ind == 0:
        return
    parent_ind = (ind - 1) // 2
    if heap[parent_ind] > heap[ind]:
        t = heap[ind]
        heap[ind] = heap[parent_ind]
        heap[parent_ind] = t
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

def structure():
    if not heap:
        print("---STRUCTURE START---\n---STRUCTURE END---")
        return

    dfsArray = [0]
    print("---STRUCTURE START---")
    while dfsArray:
        print(" ".join(str(heap[i]) for i in dfsArray))
        newInd = []
        for index in dfsArray:
            left, right = 2 * index + 1, 2 * index + 2
            if left < len(heap): newInd.append(left)
            if right < len(heap): newInd.append(right)
        dfsArray = newInd
    print("---STRUCTURE END---")
    return

def add(v: int) -> str:
    heap.append(v)
    sift_up(len(heap) - 1)
    return "ok"

def find_min():
    return heap[0]

def size():
    return len(heap)

if __name__ == "__main__":
    heap = []

    while True:
        message = input().strip().split()
        if message[0] == "add":
            print(add(int(message[1])))
        elif message[0] == "min":
            print(find_min())
        elif message[0] == "size":
            print(size())
        elif message[0] == "pop":
            print(pop())
        elif message[0] == "structure":
            structure()
        elif message[0] == "exit":
            print("bye")
            break