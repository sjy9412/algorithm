T = int(input())
for tc in range(1, T + 1):
    N, M, K = map(int, input().split())
    die = set()
    active = dict()
    inactive = dict()
    for i in range(N):
        tmp = list(map(int, input().split()))
        for j in range(M):
            if tmp[j]:
                inactive[(i, j)] = [tmp[j], tmp[j]]
    act = dict()
    for k in range(K):
        inact = dict()
        for key, value in act.items():
            for dx, dy in (0, 1), (0, -1), (1, 0), (-1, 0):
                tx, ty = key[0] + dx, key[1] + dy
                if (tx, ty) not in die and not inactive.get((tx, ty), 0) and not active.get((tx, ty), 0):
                    life = inact.get((tx, ty), 0)
                    if not life or life[1] < value[1]:
                        inact[(tx, ty)] = [value[1], value[1]]
        tdie = set()
        act = dict()
        for key, value in inactive.items():
            if value[0] > 1:
                inactive[key][0] -= 1
            else:
                act[key] = [value[1], value[1]]
        for key, value in active.items():
            if value[0] > 1:
                active[key][0] -= 1
            else:
                tdie.add(key)
        for key in act:
            inactive.pop(key)
        for key in tdie:
            active.pop(key)
        inactive.update(inact)
        active.update(act)
        die = die | tdie
    print('#{}'.format(tc), len(inactive) + len(active))