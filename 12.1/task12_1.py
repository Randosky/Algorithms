class Heap:
    def __init__(self):
        self.array = []

    def sift_up(self, ind):
        if ind == 0:
            return
        p = (ind - 1) // 2
        if self.array[p] > self.array[ind]:
            t = self.array[ind]
            self.array[ind] = self.array[p]
            self.array[p] = t
            self.sift_up(p)

    def add(self, value):
        self.array.append(value)
        self.sift_up(len(self.array) - 1)

    def min(self):
        return self.array[0]

    def size(self):
        return len(self.array)


heap = Heap()
while True:
    cmd = input().strip().split()
    if cmd[0] == "add":
        heap.add(int(cmd[1]))
        print("ok")
    elif cmd[0] == "min":
        print(heap.min())
    elif cmd[0] == "size":
        print(heap.size())
    elif cmd[0] == "exit":
        print("bye")
        break
