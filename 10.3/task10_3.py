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
            return [t, "Такой банки нет"]
        else:
            return [t, "Такая банка есть"]

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

    def min(self, node, minimum):
        if not node:
            return minimum

        if node.value < minimum:
            minimum = self.min(node.left, node.value)
        else:
            minimum = self.min(node.left, minimum)

        return minimum

    def max(self, node, maximum):
        if not node:
            return maximum

        if node.value > maximum:
            maximum = self.max(node.right, node.value)
        else:
            maximum = self.max(node.right, maximum)

        return maximum

    def printTree(self, node):
        if not node:
            return

        self.printTree(node.left)
        print(node.value, end=" ")
        self.printTree(node.right)


arr = list(map(int, input().split()))
tree = Tree().makeTree(arr)
while True:
    cmd = input().strip().split()
    if cmd[0] == "list":
        tree.printTree(tree.root)
        print()
    elif cmd[0] == "delete":
        tree.delete(int(cmd[1]))
        print("Ok")
    elif cmd[0] == "find":
        print(tree.find(int(cmd[1]))[1])
    elif cmd[0] == "add":
        tree.add(int(cmd[1]))
        print("Ok")
    elif cmd[0] == "min":
        mm = tree.min(tree.root, 1000000)
        print("Склад пуст" if mm == 1000000 else mm)
    elif cmd[0] == "max":
        mx = tree.max(tree.root, -1)
        print("Склад пуст" if mx == -1 else mx)
    elif cmd[0] == "exit":
        break
