def back(n, c1, c2):
    global MIN
    if n > MIN or n > 10:
        return
    for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
        tx1, ty1 = c1[0] + dx, c1[1] + dy
        tx2, ty2 = c2[0] + dx, c2[1] + dy
        if -1 < tx1 < N and -1 < tx2 < N and -1 < ty1 < M and -1 < ty2 < M:
            if board[tx1][ty1] != '#' and board[tx2][ty2] != '#':
                back(n + 1, (tx1, ty1), (tx2, ty2))
            elif board[tx1][ty1] != '#':
                back(n + 1, (tx1, ty1), c2)
            elif board[tx2][ty2] != '#':
                back(n + 1, c1, (tx2, ty2))
        elif not(-1 < tx1 < N and -1 < ty1 < M) and not (-1 < tx2 < N and -1 < ty2 < M):
            continue
        else:
            MIN = min(n, MIN)

N, M = map(int, input().split())
board = []
for _ in range(N):
    board.append(list(input()))
coins = []
MIN = 11
for i in range(N):
    for j in range(M):
        if board[i][j] == 'o':
            coins.append((i, j))
    if len(coins) == 2:
        break
back(1, coins[0], coins[1])
print(MIN if MIN != 11 else -1)
