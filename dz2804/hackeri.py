def Kruskal(n, edges, leaf):
    edges.sort()
    dsu = DSU(range(1, n + 1))
    deg = [0] * (n + 1)
    tw = 0
    cnt = 0

    for w, u, v in edges:
        if dsu.find(u) == dsu.find(v):
            continue
        if u in leaf and deg[u] >= 1:
            continue
        if v in leaf and deg[v] >= 1:
            continue
        dsu.union(u, v)
        deg[u] += 1
        deg[v] += 1
        tw += w
        cnt += 1
        if cnt == n - 1:
            break
    if cnt != n - 1:
        return 'impossible'
    return tw


class DSU:
    def __init__(self, vertices):
        self.parent = {v: v for v in vertices}
        self.rank = {v: 0 for v in vertices}
    def find(self, v):
        if self.parent[v] != v:
            self.parent[v] = self.find(self.parent[v])
        return self.parent[v]
    def union(self, a, b):
        a = self.find(a)
        b = self.find(b)
        if a == b:
            return
        if self.rank[a] < self.rank[b]:
            self.parent[a] = b
        elif self.rank[a] > self.rank[b]:
            self.parent[b] = a
        else:
            self.parent[b] = a
            self.rank[a] += 1


n, m, p = map(int, input().split())
G = []

if p > 0:
    hack = set(map(int, input().split()))
else:
    hack = set()


for i in range(m):
    u, v, l = map(int, input().split())
    G.append((l, u, v))

print(Kruskal(n, G, hack))