def dfs(x, y, chk, h, n, visit):
    global result
    for i in range(4):
        tx, ty = x + dx[i], y + dy[i]
        if -1 < tx < N and -1 < ty < N and (tx, ty) != visit:
            if board[tx][ty] < h:
                dfs(tx, ty, chk, board[tx][ty], n + 1, (x, y))
            elif not chk:
                for k in range(1, K + 1):
                    if board[tx][ty] - k < h:
                        dfs(tx, ty, 1, board[tx][ty] - k, n + 1, (x, y))
                        break
    result = max(result, n)


T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    board = []
    for _ in range(N):
        board.append(list(map(int, input().split())))
    dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
    MAX = max(map(max, board))
    result = 0
    for i in range(N):
        for j in range(N):
            if board[i][j] == MAX:
                dfs(i, j, 0, MAX, 1, (-1, -1))
    print('#{}'.format(tc), result)