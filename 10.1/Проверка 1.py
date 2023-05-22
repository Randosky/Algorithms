class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.root = None

    def makeTreeRecursive(self, array, left, right):
        if left + 1 > right:
            return Node(array[right])
        if left + 1 == right:
            return Node(array[left])
        m = (left + right) // 2
        t = Node(array[m])
        t.left = self.makeTreeRecursive(array, left, m)
        t.right = self.makeTreeRecursive(array, m + 1, right)
        return t

    def makeTree(self, array):
        res = Tree()
        res.root = self.makeTreeRecursive(array, 0, len(array))
        return res

    def printTree(self, node, prefix="", root=True, last=True):
        print(prefix + ("" if root else ("└───" if last else "├───")) + (str(node.value) if node else ""))
        if not node or (not node.left and not node.right):
            return
        v = [node.left, node.right]
        for i in range(len(v)):
            self.printTree(v[i], prefix + ("" if root else ("    " if last else "│   ")), False, i + 1 >= len(v))


arr = list(map(int, input().split()))
tree = Tree().makeTree(arr)
tree.printTree(tree.root)