N, M = map (int, input().split())

graph = {i:set() for i in range(N)}


for _ in range(M):
    v1, v2 = map(int, input().split())
    graph[v1].add(v2)
    graph[v2].add(v1)


def dfs(g, v):
    color[v] = 'gray'
    for i in g[v]:
        if color[i] == 'white':
            parent[i] = v
            dfs(g, i)
    color[v] = 'black'

c = 0
n = 0
for i in range(len(graph)):
    if len(graph[i])%2 != 0:
        c = c+1
        n = i
print(c)
if c == 0:
    color = ['white' for i in range(N)]
    parent = [-1] * N
    dfs(graph, 0)
    print(parent)
elif c == 2:
    color = ['white' for i in range(N)]
    parent = [-1] * N
    dfs(graph, n)
    print(parent)
else:
    print('nah')




