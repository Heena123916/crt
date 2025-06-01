def bfs(adj):
    v = len(adj)
    visited = [0] * v
    startNode = 0
    ans = []
    q = []
    if visited[startNode] == 0:
        visited[startNode] = 1
        q = [startNode]
        while q:
            node = q.pop(0)
            ans.append(node)
            for i in adj[node]:
                if visited[i] == 0:
                    visited[i] = 1
                    q.append(i)
    return ans

# Example usage
adjacency_list = [[1, 2], [0, 3], [0, 4], [1], [2]]
print(bfs(adjacency_list))
