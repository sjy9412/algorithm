T = int(input())
move = {(-1, 0): [1, 2, 5, 6], (1, 0): [1, 2, 4, 7],
        (0, -1): [1, 3, 4, 5], (0, 1): [1, 3, 6, 7]}
pipe = {1: [(-1, 0), (1, 0), (0, -1), (0, 1)], 2: [(-1, 0), (1, 0)], 3: [(0, -1), (0, 1)],
        4: [(-1, 0), (0, 1)], 5: [(1, 0), (0, 1)], 6: [(1, 0), (0, -1)], 7: [(-1, 0), (0, -1)]}
for tc in range(1, T + 1):
    N, M, R, C, L = map(int, input().split())
    board = []
    for _ in range(N):
        board.append(list(map(int, input().split())))
    tmp = [(R, C)]
    visit = [[0] * M for _ in range(N)]
    visit[R][C] = time = cnt = 1
    while tmp and time < L:
        for _ in range(len(tmp)):
            x, y = tmp.pop(0)
            for dx, dy in pipe[board[x][y]]:
                tx, ty = x + dx, y + dy
                if -1 < tx < N and -1 < ty < M and not visit[tx][ty] and board[tx][ty] in move[(dx, dy)]:
                    visit[tx][ty] = 1
                    cnt += 1
                    tmp.append((tx, ty))
        time += 1
    print('#{}'.format(tc), cnt)
