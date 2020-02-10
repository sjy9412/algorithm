dir = {0: (-1, 0), 1: (1, 0), 2: (0, -1), 3: (0, 1)}
T= int(input())
for tc in range(1, T + 1):
    N = int(input())
    nodes = {}
    for _ in range(N):
        x, y, d, k = map(int, input().split())
    nodes[(x, y)] = [dir[d], k]
    while True:
        for key in nodes:
            d, k = nodes[key]
            dx, dy = d
            if nodes.get(key, 0):

            nodes[key].pop()


