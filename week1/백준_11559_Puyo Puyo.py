def move():
    for j in range(6):
        i = 11
        while i > -1:
            chk = False
            if i > 0 and board[i][j] == '.':
                for k in range(i):
                    board[i - k][j] = board[i - 1 - k][j]
                    if board[i - 1 - k][j] != '.':
                        chk = True
            else:
                i -= 1
            if not chk:
                break



board = []
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
for _ in range(12):
    board.append(list(input()))
chk = True
while chk:
    for i in range(11, -1, -1):
        for j in range(6):
            if board[i][j] != '.':
                color = board[i][j]
                tmp = [(i, j)]
                puyo = [(i, j)]
                while tmp:
                    x, y = tmp.pop(0)
                    for k in range(4):
                        tx, ty = x + dx[k], y + dy[k]
                        if -1 < tx < 12 and -1 < ty < 6 and board[tx][ty] == color and (tx, ty) not in puyo:
                            tmp.append((tx, ty))
                            puyo.append((tx, ty))
                if len(puyo) >= 4:
                    for x, y in puyo:
                        board[x][y] = '.'
move()
