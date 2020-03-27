def back(n, cnt):
    global MIN
    if n == N or not cnt:
        MIN = min(MIN, cnt)
        return
    for j in range(W):
        for i in range(H):
            if board[i][j]:
                tmp = [[0 for _ in range(W)] for _ in range(H)]
                for x in range(H):
                    for y in range(W):
                        tmp[x][y] = board[x][y]
                t = [(i, j, board[i][j])]
                board[i][j] = 0
                while t:
                    x, y, K = t.pop(0)
                    for k in range(1, K):
                        for dx, dy in (0, 1), (0, -1), (1, 0), (-1, 0):
                            tx, ty = x + (dx * k), y + (dy * k)
                            if -1 < tx < H and -1 < ty < W and board[tx][ty]:
                                t.append((tx, ty, board[tx][ty]))
                                board[tx][ty] = 0
                cnt = 0
                for y in range(W):
                    t = []
                    for x in range(H - 1, -1, -1):
                        if not board[x][y]:
                            t.append((x, y))
                        else:
                            cnt += 1
                            if t:
                                tx, ty = t.pop(0)
                                board[tx][ty] = board[x][y]
                                board[x][y] = 0
                                t.append((x, y))
                back(n + 1, cnt)
                for x in range(H):
                    for y in range(W):
                        board[x][y] = tmp[x][y]
                break


T = int(input())
for tc in range(1, T + 1):
    N, W, H = map(int, input().split())
    board = []
    MIN = 0xffff
    for _ in range(H):
        board.append(list(map(int, input().split())))
    back(0, MIN)
    print('#{}'.format(tc), MIN)