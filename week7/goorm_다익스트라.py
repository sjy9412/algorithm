from queue import PriorityQueue


def dijkstra(s):
    D = [0xfffff] * (N + 1)
    visit = [0] * (N + 1)
    D[s] = 0
    Q = PriorityQueue()
    Q.put((0, s))
    while not Q.empty():
        d, u = Q.get()
        if d > D[u]:
            continue
        visit[u] = 1
        for v, w in node[u]:
            if not visit[v] and D[v] > D[u] + w:
                D[v] = D[u] + w
                Q.put((D[v], v))
    for i in range(1, N + 1):
        print('{}: {}'.format(i, D[i]))


N, E = map(int, input().split())
node = [[] for _ in range(N + 1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    node[u].append((v, w))
    node[v].append((u, w))
start = int(input())
dijkstra(start)