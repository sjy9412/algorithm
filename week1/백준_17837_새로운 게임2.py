N, K = map(int, input().split())
board = []
node, up = dict(), dict()
dir = {1: (0, 1), 2: (0, -1), 3: (-1, 0), 4: (1, 0)}
turn = {1: 2, 2: 1, 3: 4, 4: 3}
cnt, chk = -1, False
for _ in range(N):
    board.append(list(map(int, input().split())))
for k in range(K):
    x, y, d = map(int, input().split())
    node[k + 1] = [x - 1, y - 1, d]
    up[(x - 1, y - 1)] = [k + 1]
for c in range(1, 1000 * K + 1):
    num = c % K if c % K else K
    x, y, d = node[num]
    if not -1 < x + dir[d][0] < N or not -1 < y + dir[d][1] < N or board[x + dir[d][0]][y + dir[d][1]] == 2:
        node[num][2] = turn[d]
    tx, ty = x + dir[node[num][2]][0], y + dir[node[num][2]][1]
    if not -1 < tx < N or not -1 < ty < N or board[tx][ty] == 2:
        pass
    else:
        idx = up[(x, y)].index(num)
        tmp = up[(x, y)][idx:]
        up[(x, y)] = up[(x, y)][:idx]
        if not idx:
            up.pop((x, y))
        if board[tx][ty] == 1:
            tmp.reverse()
        if up.get((tx, ty), 0):
            up[(tx, ty)] += tmp
        else:
            up[(tx, ty)] = tmp
        for t in tmp:
            node[t][0], node[t][1] = tx, ty
    for key in up:
        if len(up[key]) >= 4:
            cnt = (c - 1) // K + 1
            chk = True
            break
    if chk:
        break
print(cnt)