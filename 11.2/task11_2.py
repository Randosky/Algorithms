def find_LCA(root, res=[]):
    if root not in vertexes.keys():
        if root == v_1:
            return 1, res
        if root == v_2:
            return 1, res
        return 0, res

    s = 0
    for i in range(len(vertexes[root])):
        r = find_LCA(vertexes[root][i], res)
        s += r[0]
        res = r[1]

    if root == v_1:
        s += 1
    if root == v_2:
        s += 1

    if s == 2 and len(res) == 0:
        res.append(root)

    return s, res


n = int(input())
vertexes = dict(eval(input()))
v_1, v_2 = map(int, input().split())

print(find_LCA(list(vertexes.keys())[0])[1][0])