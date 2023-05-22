class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None

    def makeTreeRecursive(self, array):
        if not array:
            return None

        m = (len(array)) // 2
        if len(array) % 2 == 0:
            m -= 1

        t = Node(array[m])
        t.left = self.makeTreeRecursive(array[:m])
        t.right = self.makeTreeRecursive(array[m + 1:])
        return t

    def makeTree(self, array):
        res = Tree()
        res.root = self.makeTreeRecursive(array)
        return res

    def printTree(self, node, prefix="", root=True, last=True):
        if not node:
            return

        print(prefix + ("" if root else ("└───" if not node.left and last or node.left and last else "├───")) + str(node.value))
        if node.left or node.right:
            self.printTree(node.left, prefix + ("" if root else ("    " if  last else "│   ")), False, False)
            self.printTree(node.right, prefix + ("" if root else ("    " if last else "│   ")), False, True)


arr = list(map(int, input().split()))
tree = Tree().makeTree(arr)
tree.printTree(tree.root)