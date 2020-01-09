N = int(input())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))
MIN = 0xffff
for d1 in range(1, N - 1):
    for d2 in range(1, N - 1):
        if d1 + d2 >= N: break
        for i in range(N - d1 - d2):
            for j in range(d1, N - d2):
                cnt = [0] * 5
                t1 = t2 = 0
                t3 = d2
                t4 = d1
                for x in range(N):
                    if i <= x < i + d1:
                        t1 += 1
                    elif i + d1 < x <= i + d1 + d2:
                        t3 -= 1
                    if i < x <= i + d2:
                        t2 += 1
                    elif i + d2 + 1 < x <= i + d1 + d2 + 1:
                        t4 -= 1
                    for y in range(N):
                        if 0 <= x < i + d1 and 0 <= y <= j - t1:
                            cnt[0] += board[x][y]
                        elif 0 <= x <= i + d2 and j + t2 < y <= N - 1:
                            cnt[1] += board[x][y]
                        elif i + d1 <= x <= N - 1 and 0 <= y < j - d1 + d2 - t3:
                            cnt[2] += board[x][y]
                        elif i + d2 < x <= N - 1 and j - d1 + d2 + t4 <= y <= N - 1:
                            cnt[3] += board[x][y]
                        else:
                            cnt[4] += board[x][y]
                MIN = min(MIN, max(cnt) - min(cnt))
print(MIN)
