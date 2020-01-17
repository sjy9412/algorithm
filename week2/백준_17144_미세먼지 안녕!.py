R, C, T = map(int, input().split())
board = []
for _ in range(R):
    board.append(list(map(int, input().split())))
for k in range(R):
    if board[k][0] == -1:
        air = k
        break
for sec in range(T):
    tmp = [[0] * C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if board[i][j] > 0:
                cnt, dust = 0, board[i][j]//5
                for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    tx, ty = i + dx, j + dy
                    if -1 < tx < R and -1 < ty < C and board[tx][ty] != -1:
                        tmp[tx][ty] += dust
                        cnt += 1
                tmp[i][j] += board[i][j] - cnt * dust
    for i in range(R):
        for j in range(C):
            if board[i][j] == -1:
                continue
            if j == 0 and 0 < i < air or j == C - 1 and i > air + 1:
                t = tmp[i - 1][j]
            elif j == 0 and R - 1 > i > air or j == C - 1 and i < air:
                t = tmp[i + 1][j]
            elif j < C - 1 and (i == 0 or i == R - 1):
                t = tmp[i][j + 1]
            elif j > 0 and (i == air or i == air + 1):
                if j == 1:
                    t = 0
                else:
                    t = tmp[i][j - 1]
            else:
                t = tmp[i][j]
            board[i][j] = t
print(sum(map(sum, board)) + 2)