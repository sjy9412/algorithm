def chk(board):
    c = 0
    for j in range(W):
        MAX = 0
        tmp, k = board[0][j], 1
        for i in range(1, D):
            if tmp == board[i][j]:
                k += 1
            else:
                MAX = max(MAX, k)
                tmp, k = board[i][j], 1
        MAX = max(MAX, k)
        if MAX < K:
            return False
    return True


def back(n, board, cnt):
    global MIN
    if chk(board):
        MIN = min(MIN, cnt)
        return
    if n >= D:
        return
    tmp = board[n][:]
    back(n + 1, board, cnt)
    if cnt + 1 < MIN <= K:
        board[n] = [0] * W
        back(n + 1, board, cnt + 1)
        board[n] = tmp[:]
        board[n] = [1] * W
        back(n + 1, board, cnt + 1)
        board[n] = tmp[:]


T = int(input())
for tc in range(1, T + 1):
    D, W, K = map(int, input().split())
    board = []
    for _ in range(D):
        board.append(list(map(int, input().split())))
    MIN = K
    back(0, board, 0)
    print('#{}'.format(tc), MIN)