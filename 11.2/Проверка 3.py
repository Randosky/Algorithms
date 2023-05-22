def lowest_common_ancestor(vertex, ans, x, y):
    if vertex in tree.keys():
        total_sum = 0
        for child in range(len(tree[vertex])):
            response = lowest_common_ancestor(tree[vertex][child], ans, x, y)
            total_sum += response[0]
            ans = response[1]

        if vertex == x:
            total_sum += 1
        if vertex == y:
            total_sum += 1

        if total_sum == 2 and ans == -1:
            ans = vertex

        return total_sum, ans
    else:
        if vertex == x or vertex == y:
            return 1, ans
        else:
            return 0, ans


if __name__ == "__main__":
    n = int(input())
    tree = eval(input())
    a, b = map(int, input().split())

    print(lowest_common_ancestor(list(tree.keys())[0], -1, a, b)[1])
