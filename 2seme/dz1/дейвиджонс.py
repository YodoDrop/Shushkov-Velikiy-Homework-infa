import heapq

M = int(input())

G= {}

for  i in range(M):
    v1,v2,w = input().split()
    w = float(w)
    if v1 in G:
        G[v1][v2]=w
    else:
        G[v1] = {v2:w}
    if  v2 in G:                #для не ориент графа
        G[v2][v1] = w
    else:
        G[v2]={v1:w}



def belford(G, s):
    dist = {v:float('inf') for v in G}
    dist[s] = 0
    for _ in range(len(G) - 1):
        for v in G:
            for u in G[v]:
                if dist[u] > dist[v]+G[v][u]:
                    dist[u] = dist[v]+G[v][u]
    dist1 = dist.copy()
    for v in G:
        for u in G[v]:
            if dist[u] > dist[v] + G[v][u]:
                dist[u] = dist[v] + G[v][u]
    if dist1 == dist:
        return dist
    else:
        return False


def pot_func(G):
    s = 's'
    G[s] = {}
    for i in G:
        if i == s:
            continue
        G[s][i] = 0
    dist = belford(G, s)
    del G['s']
    if dist:
        for v in G:
            for u in G[v]:
                G[v][u] = G[v][u] + dist[v] - dist[u]

def djikstra(G, start):
    distances = {v:float('inf') for v in G}
    distances[start] = 0
    h = [(0, start)]
    while h:
        cur_dist, cur_node = heapq.heappop()
        if cur_dist > distances[cur_node]:
            continue
        for neighbour in G[cur_node]:
            distance = cur_dist + G[cur_node][neighbour]
            if distance < distances[neighbour]:
                distances[neighbour] = distance
                heapq.heappush((h,(distance, neighbour)))
    return distances

