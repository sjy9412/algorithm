R, C, M = map(int, input().split())
board = dict()
dir = {1: (-1, 0), 2: (1, 0), 3: (0, 1), 4: (0, -1)}
turn = {1: 2, 2: 1, 3: 4, 4: 3}
for _ in range(M):
    r, c, s, d, z = map(int, input().split())
    board[(r - 1, c - 1)] = [s, d, z]
result = 0
for i in range(C):
    for j in range(R):
        fish = board.get((j, i), 0)
        if fish:
            result += fish[2]
            board.pop((j, i))
            break
    tmp = dict()
    for key in board:
        x, y = key
        s, d, z = board[key]
        dx, dy = dir[d]
        tx, ty = abs(dx) * s % ((R - 1) * 2), abs(dy) * s % ((C - 1) * 2)
        for _ in range(tx):
            if x + dx == -1 or x + dx == R:
                d = turn[d]
                dx, dy = dir[d]
            x += dx
        for _ in range(ty):
            if y + dy == -1 or y + dy == C:
                d = turn[d]
                dx, dy = dir[d]
            y += dy
        if tmp.get((x, y), 0) and tmp[(x, y)][2] > z:
            continue
        tmp[(x, y)] = [s, d, z]
    board = dict(tmp)
print(result)
