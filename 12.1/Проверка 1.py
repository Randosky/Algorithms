class Heap:
    def __init__(self):
        self.array = [0]

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
        ind = len(self.array)
        self.array.append(value)
        self.sift_up(ind)

    def sift_down(self, ind):
        left = 2 * ind
        right = 2 * ind + 1
        smallest = ind

        if left < len(self.array) and self.array[left] < self.array[ind]:
            smallest = left

        if right < len(self.array) and self.array[right] < self.array[smallest]:
            smallest = right

        if smallest != ind:
            self.array[ind], self.array[smallest] = self.array[smallest], self.array[ind]
            self.sift_down(smallest)

    def extract_min(self):
        minimum = self.array[0]
        self.array[0] = self.array[-1]
        self.array.pop()
        self.sift_down(0)
        return minimum

    def size(self):
        return len(self.array) - 1


heap = Heap()
while True:
    cmd = input().strip().split()
    if cmd[0] == "add":
        heap.add(int(cmd[1]))
        print("ok")
    elif cmd[0] == "min":
        print(heap.extract_min())
    elif cmd[0] == "size":
        print(heap.size())
    elif cmd[0] == "exit":
        print("bye")
        break
