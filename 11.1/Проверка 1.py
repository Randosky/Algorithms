def bfs(graph, start):
    visited = [start]
    queue = [start]
    while queue:
        vertex = queue.pop()
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
    return visited

n, v = map(int, input().split())
vertexes = {}
for i in range(n):
    neighbours = list(map(int, input().split()))
    vertexes[i] = [j for j in neighbours if j != -1]

print(' '.join(map(str, sorted(bfs(vertexes, v)))))
