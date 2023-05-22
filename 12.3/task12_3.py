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
            return self.array.pop()
        min_value = self.array[0]
        self.array[0] = self.array.pop()
        self.sift_down(0)
        return min_value

heap = Heap()
n, bag = map(int, input().split())

for _ in range(n):
    price, volume = map(int, input().split())
    heap.add((-price / volume, price, volume))

final_cost = 0
for _ in range(heap.size()):
    cake = heap.pop()
    if bag >= cake[2]:
        bag -= cake[2]
        final_cost += cake[1]
    else:
        final_cost += bag * (cake[0] * -1)
        break

print('{:.2f}'.format(final_cost))