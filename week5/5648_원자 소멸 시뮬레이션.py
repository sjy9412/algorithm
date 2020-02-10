dir = {0: (1, 0), 1: (-1, 0), 2: (0, -1), 3: (0, 1)}
T= int(input())
for tc in range(1, T + 1):
    N = int(input())
    nodes = {}
    for _ in range(N):
        y, x, d, k = map(int, input().split())
        nodes[(x * 2, y * 2)] = [dir[d], k]
    result = 0
    for _ in range(4001):
        tmp = {}
        for key, value in nodes.items():
            d, k = value
            tx, ty = key[0] + d[0], key[1] + d[1]
            if -2001 < tx < 2001 and -2001 < ty < 2001:
                if tmp.get((tx, ty), 0):
                    tmp[(tx, ty)].append(k)
                else:
                    tmp[(tx, ty)] = [d, k]
        nodes = {}
        for key, value in tmp.items():
            if len(value) > 2:
                result += sum(value[1:])
            else:
                nodes[key] = value
        if len(nodes) < 2:
            break
    print('#{}'.format(tc), result)