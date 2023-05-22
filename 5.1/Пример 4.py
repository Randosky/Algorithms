class Queue:
    a = []
    b = []

    def push(self, x):
        self.a.append(x)

    def pop(self):
        if not len(self.b):
            while len(self.a):
                self.b.append(self.a.pop())
        return self.b.pop()

    def front(self):
        if len(self.b):
            return self.b[len(self.b) - 1]
        return self.a[0]

    def size(self):
        return len(self.a) + len(self.b)

    def view(self):
        b_r = self.b
        b_r.reverse()
        return b_r + self.a

    def clear(self):
        self.a.clear()
        self.b.clear()

queue = Queue()
result = []

while True:
    line = input().strip()
    if line.startswith("push"):
        _, value = line.split()
        queue.push(value)
        result.append("ok")
        continue
    elif line == "pop":
        result.append(queue.pop())
        continue
    elif line == "front":
        result.append(queue.front())
        continue
    elif line == "size":
        result.append(queue.size())
        continue
    elif line == "view":
        result.append(", ".join(queue.view()))
        continue
    elif line == "clear":
        queue.clear()
        result.append("ok")
        continue
    elif line == "exit":
        result.append("bye")
        break

print(*result, sep="\n")