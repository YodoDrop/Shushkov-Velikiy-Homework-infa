import math
n = int(input())
m = int(input())
INF = float("inf")


G = [[INF] * m for _ in range(m)]


for i in range(n):
    v1, v2, w = map(int, input().split())
    w = -math.log(float(w))
    G[v1][v2] = w


def minus_floyd(dist):
    n = len(dist)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    for i in range(n):
        if dist[i][i] < 0:
            return True
    return False

print(minus_floyd(G))
