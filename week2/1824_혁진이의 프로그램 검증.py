def back(dx, dy):
    global x, y, result, memory
    while True:
        cmd = board[x][y]
        if cmd == '@':
            result = 'YES'
            return
        elif cmd == '.':
            pass
        elif cmd == '+':
            memory = 0 if memory == 15 else memory + 1
        elif cmd == '-':
            memory = 15 if memory == 0 else memory - 1
        elif cmd.isdecimal():
            memory = int(cmd)
        elif cmd == '?':
            for dx, dy in (1, 0), (-1, 0), (0, -1), (0, 1):
                tx = 0 if x + dx == R else R - 1 if x + dx == -1 else x + dx
                ty = 0 if y + dy == C else C - 1 if y + dy == -1 else y + dy
                if (memory, dx, dy) in visit[tx][ty]:
                    continue
                tmp = (memory, x, y)
                visit[tx][ty].append((memory, dx, dy))
                x, y = tx, ty
                back(dx, dy)
                visit[tx][ty].pop()
                memory, x, y = tmp
        elif cmd == '<' or cmd == '_' and memory:
            dx, dy = 0, -1
        elif cmd == '>' or cmd == '_':
            dx, dy = 0, 1
        elif cmd == '^' or cmd == '|' and memory:
            dx, dy = -1, 0
        else:
            dx, dy = 1, 0
        x = 0 if x + dx == R else R - 1 if x + dx == -1 else x + dx
        y = 0 if y + dy == C else C - 1 if y + dy == -1 else y + dy
        if (memory, dx, dy) in visit[x][y]:
            return
        visit[x][y].append((memory, dx, dy))

T = int(input())
for tc in range(1, T + 1):
    R, C = map(int, input().split())
    board = []
    for _ in range(R):
        board.append(input())
    visit = [[[] for _ in range(C)] for _ in range(R)]
    x = y = memory = 0
    result, chk = 'NO', False
    can = [('<', '|', '^', 'v'), ('>', '|', '^', 'v'), ('^', '_', '>', '<'), ('v', '_', '>', '<')]
    for i in range(R):
        for j in range(C):
            if board[i][j] == '@' and (i != 0 and board[i - 1][j] not in can[2] or i != R - 1 and board[i + 1][j] not in can[3] or j != 0 and board[i][j - 1] not in can[0] or j != C - 1 and board[i][j + 1] not in can[1]):
                chk = True
    if chk:
        back(0, 1)
    print('#{}'.format(tc), result)