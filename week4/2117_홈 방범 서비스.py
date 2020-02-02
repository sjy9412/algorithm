T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    board = []
    total = 0
    for _ in range(N):
        tmp = list(map(int, input().split()))
        board.append(tmp)
        total += sum(tmp)
    MAX = 0
    for i in range(N):
        for j in range(N):
            visit = [[0] * N for _ in range(N)]
            cnt = 1 if board[i][j] else 0
            tmp = [(i, j)]
            visit[i][j] = 1
            k = 0
            while tmp and k < N + 1:
                k += 1
                if total * M - (k ** 2 + (k - 1) ** 2) < 0:
                    break
                if cnt * M - (k ** 2 + (k - 1) ** 2) >= 0 and MAX < cnt:
                        MAX = cnt
                for _ in range(len(tmp)):
                    x, y = tmp.pop(0)
                    for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
                        tx, ty = x + dx, y + dy
                        if -1 < tx < N and -1 < ty < N and not visit[tx][ty]:
                            tmp.append((tx, ty))
                            visit[tx][ty] = 1
                            if board[tx][ty]:
                                cnt += 1
    print('#{}'.format(tc), MAX)