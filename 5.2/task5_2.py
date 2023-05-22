class Node:
    def __init__(self, p, i):
        self.profession = p
        self.importance = i
        self.next = None
        self.prev = None


class Queue:
    length = 0

    def __init__(self):
        self.start = None
        self.end = None

    def push(self, p, i):
        tmp = Node(p, i)
        if self.end is None:
            self.start = tmp
            self.end = tmp
            self.length += 1
            return "ok"
        tmp.next = None
        self.end.next = tmp
        tmp.prev = self.end
        self.end = tmp
        self.length += 1
        return "ok"

    def delete(self, node):
        v_next = node.next
        v_prev = node.prev

        if v_prev is not None:
            v_prev.next = v_next
        if v_next is not None:
            v_next.prev = v_prev

        node.prev = None
        node.next = None

        if node == self.start:
            self.start = v_next
        if node == self.end:
            self.end = v_prev

        return node.profession, v_next

    def popTop(self):
        if self.end is None or self.start is None:
            return -1

        tmp = self.start
        maxImpNode = self.start
        while tmp is not None:
            if tmp.importance > maxImpNode.importance:
                maxImpNode = tmp
            tmp = tmp.next

        self.length -= 1
        return self.delete(maxImpNode)[0]

    def pop(self, i):
        tmp = self.start
        flag = False
        while tmp is not None:
            if tmp.importance == i:
                flag = True
                break
            tmp = tmp.next

        if flag:
            self.length -= 1
            return self.delete(tmp)[0]
        else:
            return -1

    def popAll(self, i):
        tmp = self.start
        result = []
        while tmp is not None:
            tmpToDel = tmp
            if tmp.importance == i:
                res = self.delete(tmpToDel)
                result.append(str(res[0]))
                self.length -= 1
                tmp = res[1]
            else:
                tmp = tmp.next

        if not result:
            return -1
        return " ".join(result)

    def size(self):
        return self.length

    def clear(self):
        self.start = None
        self.end = None
        self.length = 0
        return "ok"


queue = Queue()
answers = []

while True:
    cmd = input().strip().split()
    if cmd[0] == "push":
        answers.append(queue.push(int(cmd[1]), int(cmd[2])))
    elif cmd[0] == "pop":
        if cmd[1] == "top":
            answers.append(queue.popTop())
        else:
            answers.append(queue.pop(int(cmd[1])))
    elif cmd[0] == "popall":
        answers.append(queue.popAll(int(cmd[1])))
    elif cmd[0] == "size":
        answers.append(queue.size())
    elif cmd[0] == "clear":
        answers.append(queue.clear())
    elif cmd[0] == "exit":
        answers.append("bye")
        break

print(*answers, sep="\n")
