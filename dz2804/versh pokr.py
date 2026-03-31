def HelpDfs(g, v, n):
    color = [0 for i in range(n)]
    left = set(v)
    right = set()
    empty_set1 = set()
    empty_set2 = set()
    def Dfs(v):
        color[v] = 1
        if v in left:
            for u in g[v]:
                if color[u] == 0:
                    right.add(u)
                else:
                    if u in right:
                        continue
                    else:
                        return False
        else:
            for u in g[v]:
                if color[u] == 0:
                    left.add(u)
                else:
                    if u in left:
                        continue
                    else:
                        return False
            return True
    if Dfs(v):
        return left, right
    else:
        return empty_set1, empty_set2



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

    for u, v in edge:
        capacity = 1 # один поток у всех
        G[u][v] = G[u].get(v) + capacity
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

for i in range(n):
    u, v = map(int, input().split())
    G.append([u, v])

left, right = HelpDfs(G, 1, n)

for u in left:
    G.append([n+1, u])
for u in right:
    G.append([n+2, u])

p = EdmondsKarp(n+2, G, n+1, n+2)

print(n-p)








