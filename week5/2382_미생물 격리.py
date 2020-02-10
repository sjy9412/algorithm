T = int(input())
dir = {1: (-1, 0), 2: (1, 0), 3: (0, -1), 4: (0, 1)}
for tc in range(1, T + 1):
    N, M, K = map(int, input().split())
    group = {}
    result = 0
    for _ in range(K):
        i, j, c, d = map(int, input().split())
        group[(i, j)] = [c, dir[d]]
    for m in range(M):
        new = {}
        max = []
        for key in group:
            x, y = key
            cnt, d = group[key]
            tx, ty = x + d[0], y + d[1]
            if tx == 0 or ty == 0 or tx == N - 1 or ty == N - 1:
                cnt //= 2
                d = (d[0] * -1, d[1] * -1)
            tmp = new.get((tx, ty), 0)
            if tmp:
                if len(tmp) == 2:
                    if tmp[0] < cnt:
                        max.append((tx, ty))
                        new[(tx, ty)].append(cnt)
                        new[(tx, ty)][1] = d
                    else:
                        max.append((tx, ty))
                        new[(tx, ty)].append(tmp[0])
                elif tmp[2] < cnt:
                    new[(tx, ty)][2] = cnt
                    new[(tx, ty)][1] = d
                new[(tx, ty)][0] += cnt
            elif cnt:
                new[(tx, ty)] = [cnt, d]
            if m == M - 1:
                result += cnt
        for x, y in max:
            new[(x, y)].pop()
        group = dict(new)
    print('#{}'.format(tc), result)