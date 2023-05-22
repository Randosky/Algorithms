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

    def sift_down(self, index):
        left_child_index = 2 * index + 1
        right_child_index = 2 * index + 2
        smallest = index
        if left_child_index < len(self.array) and self.array[left_child_index] < self.array[smallest]:
            smallest = left_child_index
        if right_child_index < len(self.array) and self.array[right_child_index] < self.array[smallest]:
            smallest = right_child_index
        if smallest != index:
            self.array[index], self.array[smallest] = self.array[smallest], self.array[index]
            self.sift_down(smallest)

    def pop(self):
        if len(self.array) == 1:
            return str(self.array.pop())
        min_value = self.array[0]
        self.array[0] = self.array.pop()
        self.sift_down(0)
        return str(min_value)

    def structure(self):
        if not self.array:
            return

        queue = [0]
        while queue:
            print(*[self.array[i] for i in queue], sep=" ")
            next_indexes = []
            for index in queue:
                l_i = 2 * index + 1
                r_i = 2 * index + 2
                if l_i < len(self.array):
                    next_indexes.append(l_i)
                if r_i < len(self.array):
                    next_indexes.append(r_i)
            queue = next_indexes
        return


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
    elif cmd[0] == "structure":
        print("---STRUCTURE START---")
        heap.structure()
        print("---STRUCTURE END---")
    elif cmd[0] == "pop":
        print(heap.pop())
    elif cmd[0] == "exit":
        print("bye")
        break
