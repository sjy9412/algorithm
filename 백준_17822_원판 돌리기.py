from collections import deque

N, M, T = map(int, input().split())
board, cnt = [], N * M
for _ in range(N):
    board.append(deque(map(int, input().split())))
for _ in range(T):
    x, d, k = map(int, input().split())
    for i in range(x, N + 1, x):
        if d == 0:
            for _ in range(k):
                board[i - 1].appendleft(board[i - 1].pop())
        else:
            for _ in range(k):
                board[i - 1].append(board[i - 1].popleft())
    chk = cnt
    for i in range(N):
        for j in range(M):
            if board[i][j]:
                tmp = 0
                num = board[i][j]
                ttmp = [[i, j]]
                while ttmp:
                    x, y = ttmp.pop(0)
                    if (x, 0) != (i, j) and y == M - 1 and num == board[x][0]:
                        tmp += 1
                        board[x][0] = 0
                        ttmp.append([x, 0])
                    if (x, y + 1) != (i, j) and y != M - 1 and num == board[x][y + 1]:
                        tmp += 1
                        board[x][y + 1] = 0
                        ttmp.append([x, y + 1])
                    if (x, y - 1) != (i, j) and num == board[x][y - 1]:
                        tmp += 1
                        board[x][y - 1] = 0
                        ttmp.append([x, y - 1])
                    if (x + 1, y) != (i, j) and x != N - 1 and num == board[x + 1][y]:
                        tmp += 1
                        board[x + 1][y] = 0
                        ttmp.append([x + 1, y])
                    if (x - 1, y) != (i, j) and x != 0 and num == board[x - 1][y]:
                        tmp += 1
                        board[x - 1][y] = 0
                        ttmp.append([x - 1, y])
                if tmp:
                    cnt -= (tmp + 1)
                    board[i][j] = 0
    result = 0
    for i in range(N):
        result += sum(board[i])
    if not cnt:
        break
    if cnt == chk:
        avg = result / cnt
        for i in range(N):
            for j in range(M):
                if board[i][j] and board[i][j] > avg:
                    board[i][j] -= 1
                elif board[i][j] and board[i][j] < avg:
                    board[i][j] += 1
        result = 0
        for i in range(N):
            result += sum(board[i])
print(result)