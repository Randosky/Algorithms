class Node:
    def __init__(self, n):
        self.number = n
        self.next = None
        self.prev = None


start = None
end = None
middle = None
length = 0

def delNode(node, s, e):
    nodeNext = node.next
    nodePrev = node.prev

    if nodeNext is not None:
        nodeNext.prev = nodePrev
    if nodePrev is not None:
        nodePrev.next = nodeNext

    node.next = None
    node.prev = None

    if node == s:
        s = nodeNext
    if node == e:
        e = nodePrev

    return node.number, s, e

for i in range(int(input())):
    query = input().strip().split()
    if query[0] == '+':
        t = Node(int(query[1]))
        if end is None:
            start = t
            end = t
            middle = t
            length += 1
            continue
        t.next = None
        end.next = t
        t.prev = end
        end = t
        middle.prev = middle
        middle.next = middle.next.next
        length += 1
        continue
    elif query[0] == '*':
        t = Node(int(query[1]))
        if end is None:
            start = t
            end = t
            middle = t
            length += 1
            continue
        middle.prev = t
        middle.next = middle.next.next
        middle = t
        length += 1
        continue
    elif query[0] == '!':
        t = Node(int(query[1]))
        if end is None:
            start = t
            end = t
            middle = t
            length += 1
            continue
        t.next = start.next
        t.prev = None
        start = t
        length += 1
        continue
    elif query[0] == '-':
        n = None
        res = delNode(start, start, end)
        print(res[0])
        start = res[1]
        end = res[2]
        length -= 1
        continue
