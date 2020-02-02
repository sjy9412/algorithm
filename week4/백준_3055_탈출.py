R, C = map(int, input().split())
board = []
for _ in range(R):
    board.append(list(input()))
tmp = []
water = []
visit = [[0] * C for _ in range(R)]
for i in range(R):
    for j in range(C):
        if board[i][j] != '.' and board[i][j] != 'D':
            visit[i][j] = 1
            if board[i][j] == 'S':
                tmp.append((i, j))
                board[i][j] = '.'
            elif board[i][j] == '*':
                water.append((i, j))

time, result = 0, 'KAKTUS'
while tmp and result == 'KAKTUS':
    for _ in range(len(water)):
        x, y = water.pop(0)
        for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
            tx, ty = x + dx, y + dy
            if -1 < tx < R and -1 < ty < C and board[tx][ty] == '.':
                water.append((tx, ty))
                board[tx][ty] = '*'
                visit[tx][ty] = 1
    for _ in range(len(tmp)):
        x, y = tmp.pop(0)
        if board[x][y] == 'D':
            result = time
            break
        for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
            tx, ty = x + dx, y + dy
            if -1 < tx < R and -1 < ty < C and not visit[tx][ty]:
                tmp.append((tx, ty))
                visit[tx][ty] = 1
    time += 1
print(result)