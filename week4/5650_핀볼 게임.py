T = int(input())
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
for tc in range(1, T + 1):
    N = int(input())
    board = []
    for _ in range(N):
        board.append(list(map(int, input().split())))
    hole = [[] for _ in range(11)]
    for i in range(N):
        for j in range(N):
            if board[i][j] > 5:
                hole[board[i][j]].append((i, j))
    for k in range(6, 11):
        if hole[k]:
            board[hole[k][0][0]][hole[k][0][1]] = (hole[k][1][0], hole[k][1][1])
            board[hole[k][1][0]][hole[k][1][1]] = (hole[k][0][0], hole[k][0][1])
    MAX = 0
    for i in range(N):
        for j in range(N):
            if board[i][j] == 0:
                for k in range(4):
                    start = (i, j)
                    ball = [i, j, dx[k], dy[k]]
                    score = 0
                    while True:
                        x, y, ddx, ddy = ball
                        tx, ty = x + ddx, y + ddy
                        if not(-1 < tx < N) or not(-1 < ty < N):
                            score += 1
                            ball[0], ball[1] = tx, ty
                            ball[2], ball[3] = ddx * -1, ddy * -1
                        elif board[tx][ty] == -1 or (tx, ty) == start:
                            break
                        elif board[tx][ty] == 0:
                            ball[0], ball[1] = tx, ty
                        elif type(board[tx][ty]) == int and board[tx][ty] < 6:
                            if (board[tx][ty] == 1 and (ddx, ddy) == (1, 0)) or (board[tx][ty] == 2 and (ddx, ddy) == (-1, 0)):
                                ball[2], ball[3] = 0, 1
                            elif (board[tx][ty] == 1 and (ddx, ddy) == (0, -1)) or (board[tx][ty] == 4 and (ddx, ddy) == (0, 1)):
                                ball[2], ball[3] = -1, 0
                            elif (board[tx][ty] == 2 and (ddx, ddy) == (0, -1)) or (board[tx][ty] == 3 and (ddx, ddy) == (0, 1)):
                                ball[2], ball[3] = 1, 0
                            elif (board[tx][ty] == 3 and (ddx, ddy) == (-1, 0)) or (board[tx][ty] == 4 and (ddx, ddy) == (1, 0)):
                                ball[2], ball[3] = 0, -1
                            else:
                                ball[2], ball[3] = ddx * -1, ddy * -1
                            ball[0], ball[1] = tx, ty
                            score += 1
                        else:
                            ball[0], ball[1] = board[tx][ty]
                    MAX = max(MAX, score)
    print('#{}'.format(tc), MAX)