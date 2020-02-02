def move():
    for j in range(6):
        tmp = []
        for i in range(11, -1, -1):
            if board[i][j] == '.':
                tmp.append((i, j))
            elif tmp:
                x, y = tmp.pop(0)
                board[i][j], board[x][y] = board[x][y], board[i][j]
                tmp.append((i, j))

board = []
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
for _ in range(12):
    board.append(list(input()))
cnt = 0
while True:
    chk = False
    visit = [[0] * 6 for _ in range(12)]
    for i in range(11, -1, -1):
        for j in range(6):
            if not visit[i][j] and board[i][j] != '.':
                tmp = [(i, j)]
                nodes = [(i, j)]
                c = board[i][j]
                visit[i][j] = 1
                while tmp:
                    x, y = tmp.pop(0)
                    for k in range(4):
                        tx, ty = x + dx[k], y + dy[k]
                        if -1 < tx < 12 and -1 < ty < 6 and not visit[tx][ty] and board[tx][ty] == c:
                            tmp.append((tx, ty))
                            nodes.append((tx, ty))
                            visit[tx][ty] = 1
                if len(nodes) >= 4:
                    for x, y in nodes:
                        board[x][y] = '.'
                    chk = True
    if chk:
        move()
        cnt += 1
    else:
        break
print(cnt)