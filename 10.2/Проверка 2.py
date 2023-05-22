class Node:
    def __init__(self, value, parent):
        self.value = value
        self.parent = parent
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.root = None

    def __makeTreeRecursive(self, array):
        if not array:
            return None

        m = (len(array)) // 2
        if len(array) % 2 == 0:
            m -= 1

        t = Node(array[m], None)
        t.left = self.__makeTreeRecursive(array[:m])
        t.right = self.__makeTreeRecursive(array[m + 1:])
        if t.left is not None:
            t.left.parent = t
        if t.right is not None:
            t.right.parent = t
        return t

    def makeTree(self, array):
        res = Tree()
        res.root = self.__makeTreeRecursive(array)
        return res

    def __addRecursive(self, node, value):
        if node is None:
            return
        if value < node.value:
            if node.left is None:
                node.left = Node(value, node)
                return
            self.__addRecursive(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value, node)
                return
            self.__addRecursive(node.right, value)

    def add(self, value):
        if self.root is None:
            self.root = Node(value, None)
            return
        self.__addRecursive(self.root, value)

    def __findRecursive(self, node, value):
        if node is None:
            return None
        if node.value == value:
            return node
        if node.value > value:
            return self.__findRecursive(node.left, value)
        else:
            return self.__findRecursive(node.right, value)

    def find(self, value):
        t = self.__findRecursive(self.root, value)
        if t is None:
            return [t, "Число не нашлось"]
        else:
            return [t, "Число нашлось"]

    def __deleteRecursive(self, t):
        if t is None:
            return

        if (t.left is None) or (t.right is None):
            child = None
            if t.left is not None:
                child = t.left
            else:
                child = t.right
            if t == self.root:
                self.root = child
                if child is not None:
                    child.parent = None
            if t.parent.left == t:
                t.parent.left = child
                if child is not None:
                    child.parent = t.parent
            else:
                t.parent.right = child
                if child is not None:
                    child.parent = t.parent
        else:
            nxt = t.right
            while nxt.left is not None:
                nxt = nxt.left
            t.value = nxt.value
            self.__deleteRecursive(nxt)

    def delete(self, value):
        if self.root is None:
            return
        t = self.find(value)
        if t[0] is None:
            return
        self.__deleteRecursive(t[0])

    def next_node(self, value):
        node = self.find(value)
        node = node[0]
        if node is None:
            return "Следующего числа нет"
        if node.right is not None:
            nxt = node.right
            while nxt.left is not None:
                nxt = nxt.left
            return nxt.value
        nxt = node
        while (nxt.parent is not None) and (nxt.parent.right == nxt):
            nxt = nxt.parent
        if nxt.parent is None:
            return "Следующего числа нет"
        return nxt.parent.value

    def printTree(self, node, prefix="", root=True):
        if not node:
            return

        parentChilds = [None, None] if root else [node.parent.left, node.parent.right]
        checkLast = True
        if parentChilds[0] is not None and parentChilds[1] is not None and parentChilds[0] == node:
            checkLast = False

        print(prefix + ("" if root else ("└───" if checkLast else "├───")) + str(node.value))
        if node.left or node.right:
            self.printTree(node.left, prefix + ("" if root else ("│   " if not checkLast else "    ")), False)
            self.printTree(node.right, prefix + ("" if root else ("│   " if not checkLast else "    ")), False)

    @staticmethod
    def count_children(node):
        count = 0
        if node.left is not None:
            count += 1
        if node.right is not None:
            count += 1

        return count


arr = list(map(int, input().split()))
tree = Tree().makeTree(arr)
while True:
    cmd = input().strip().split()
    if cmd[0] == "print":
        tree.printTree(tree.root)
    elif cmd[0] == "delete":
        tree.delete(int(cmd[1]))
        print("Ok")
    elif cmd[0] == "find":
        print(tree.find(int(cmd[1]))[1])
    elif cmd[0] == "add":
        for i in range(1, len(cmd)):
            tree.add(int(cmd[i]))
        print("Ok")
    elif cmd[0] == "next":
        print(tree.next_node(int(cmd[1])))
    elif cmd[0] == "exit":
        break
