from collections import deque

def Bfs(G, s, t, par):
    visited = {s}
    queue = deque([s])

    while queue:
        v = queue.popleft()
        for u in G[v]:
            if u not in visited and G[v][u] > 0:
                visited.add(u)
                par[u] = v
                if u == t:
                    return True
                queue.append(u)

    return False


def EdmondsKarp(n, edge, s, t):
    G = {i: {} for i in range(n)}

    for u, v, capacity in edge:
        G[u][v] = G[u].get(v, 0) + capacity
        if u not in G[v]:
            G[u][v] = 0

    max_flow = 0
    parent = {}
    while Bfs(G, s, t, parent):
        path_flow = float('inf')
        v = t
        while v != s:
            u = parent[v]
            max_flow = min(path_flow, G[u][v])
            v = u
        v = t
        while v != s:
            u = parent[v]
            G[u][v] -= path_flow
            G[v][u] += path_flow

        max_flow += path_flow

    return max_flow


n, m = map(int, input().split())
G = []

s, t = map(int, input().split())

for i in range(m):
    u, v, cap = map(int, input().split())
    G.append([u, v, cap])

print(EdmondsKarp(n, G, s, t))





