def add(v):
    heap.append(v)
    sift_up(len(heap) - 1)
    return "ok"

def sift_up(ind):
    if ind == 0:
        return
    parent_ind = (ind - 1) // 2
    if heap[parent_ind] > heap[ind]:
        t = heap[ind]
        heap[ind] = heap[parent_ind]
        heap[parent_ind] = t
        sift_up(parent_ind)

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
        elif message[0] == "exit":
            print("bye")
            break