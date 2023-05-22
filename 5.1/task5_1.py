class Node:
    def __init__(self, v):
        self.value = v
        self.next = None
        self.prev = None


class Queue:
    length = 0

    def __init__(self):
        self.start = None
        self.end = None

    def push(self, v):
        tmp = Node(v)
        if self.end is None:
            self.start = tmp
            self.end = tmp
        tmp.next = None
        self.end.next = tmp
        tmp.prev = self.end
        self.end = tmp
        self.length += 1
        return "ok"

    def pop(self):
        tmp = self.start
        v_next = self.start.next

        self.start.prev = None
        self.start.next = None
        self.start = v_next

        self.length -= 1
        return tmp.value

    def front(self):
        return self.start.value

    def size(self):
        return self.length

    def view(self):
        answer = []
        tmp = self.start
        while tmp is not None:
            answer.append(tmp.value)
            tmp = tmp.next
        return answer

    def clear(self):
        self.start.next = None
        self.start = None
        self.end.prev = None
        self.end = None
        self.length = 0
        return "ok"

queue = Queue()
answers = []

while True:
    cmd = input().strip()
    if cmd.startswith("push"):
        _, value = cmd.split()
        answers.append(queue.push(value))
        continue
    elif cmd == "pop":
        answers.append(queue.pop())
        continue
    elif cmd == "front":
        answers.append(queue.front())
        continue
    elif cmd == "size":
        answers.append(queue.size())
        continue
    elif cmd == "view":
        answers.append(", ".join(queue.view()))
        continue
    elif cmd == "clear":
        answers.append(queue.clear())
        continue
    elif cmd == "exit":
        answers.append("bye")
        break

print(*answers, sep="\n")



