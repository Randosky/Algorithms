class Node:
    def __init__(self, p, i):
        self.importance = i
        self.profession = p
        self.next = None
        self.prev = None


result = []
length = 0
start = None
end = None


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

    return node.profession, nodeNext, s, e

nodeDict = {}
while True:
    message = input().strip().split()
    if message[0] == "push":
        t = Node(int(message[1]), int(message[2]))
        if int(message[2]) in nodeDict.keys():
            nodeDict[int(message[2])].append(t)
        else:
            nodeDict[int(message[2])] = [t]

        if end is None:
            start = t
            end = t
            length += 1
            result.append("ok")
            continue
        t.next = None
        end.next = t
        t.prev = end
        end = t
        length += 1
        result.append("ok")
        continue

    elif message[0] == "pop":
        if message[1] == "top":
            if end is None or start is None:
                result.append("-1")
                continue

            maxImp = max(nodeDict.keys())
            maximum = nodeDict[maxImp][0]

            if len(nodeDict[maxImp]) == 1:
                nodeDict.pop(maxImp)
            else:
                nodeDict[maxImp].remove(maximum)

            length -= 1
            res = delNode(maximum, start, end)
            start = res[2]
            end = res[3]
            result.append(res[0])
            continue
        else:
            k = int(message[1])

            if k not in nodeDict.keys():
                result.append("-1")
                continue

            t = nodeDict[k][0]
            if len(nodeDict[k]) == 1:
                nodeDict.pop(k)
            else:
                nodeDict[k].remove(t)

            length -= 1
            res = delNode(t, start, end)
            start = res[2]
            end = res[3]
            n = res[0]

            if n is not None:
                result.append(n)
            else:
                result.append("-1")
            continue
    elif message[0] == "popall":
        if int(message[1]) not in nodeDict.keys():
            result.append("-1")
            continue

        allToPopNumbers = []
        allToPop = nodeDict[int(message[1])]

        for n in allToPop:
            res = delNode(n, start, end)
            allToPopNumbers.append(str(res[0]))
            start = res[2]
            end = res[3]
            length -= 1

        nodeDict.pop(int(message[1]))
        result.append(" ".join(allToPopNumbers))
        continue

    elif message[0] == "size":
        result.append(length)
        continue

    elif message[0] == "clear":
        start = None
        end = None
        length = 0
        nodeDict.clear()
        result.append("ok")
        continue

    elif message[0] == "exit":
        result.append("bye")
        break

print(*result, sep="\n")