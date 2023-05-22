def findConnectedVertexes(visited, q):
    while q:
        vertex = q.pop()
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.append(neighbour)
                q.append(neighbour)

    return visited


if __name__ == "__main__":
    n, v = map(int, input().split())
    graph = {}
    for i in range(n):
        neighbours = list(map(int, input().split()))
        graph[i] = [j for j in neighbours if j != -1]

    print(*sorted(findConnectedVertexes([v], [v])))
