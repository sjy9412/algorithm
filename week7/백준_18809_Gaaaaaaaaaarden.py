def back(n, choice, color):
    global MAX
    if color == 'g' and len(choice) == G:
        back(0, choice, 'r')
        return
    elif color == 'r' and len(choice) == R + G:
        MAX = max(MAX, bfs(choice))
        return
    elif n == K:
        return
    if used[n] == 0:
        used[n] = 1
        back(n + 1, choice + [n], color)
        used[n] = 0
    back(n + 1, choice, color)


def bfs(choice):
    visit = [[0] * M for _ in range(N)]
    tmp_g = []
    tmp_r = []
    cnt = 0
    for i in range(R + G):
        x, y = able[choice[i]]
        if i < R:
            tmp_g.append((x, y))
        else:
            tmp_r.append((x, y))
        visit[x][y] = 1
    while tmp_g or tmp_r:
        visit_g = set()
        for _ in range(len(tmp_g)):
            x, y = tmp_g.pop(0)
            if visit[x][y] != 2:
                for k in range(4):
                    tx, ty = x + dx[k], y + dy[k]
                    if -1 < tx < N and -1 < ty < M and board[tx][ty] != 0 and visit[tx][ty] == 0:
                        visit[tx][ty] = 1
                        tmp_g.append((tx, ty))
                        visit_g.add((tx, ty))
        for _ in range(len(tmp_r)):
            x, y = tmp_r.pop(0)
            for k in range(4):
                tx, ty = x + dx[k], y + dy[k]
                if -1 < tx < N and -1 < ty < M and board[tx][ty] != 0:
                    if visit[tx][ty] == 1 and (tx, ty) in visit_g:
                        visit[tx][ty] = 2
                        cnt += 1
                    elif visit[tx][ty] == 0:
                        visit[tx][ty] = 1
                        tmp_r.append((tx, ty))
    return cnt


N, M, G, R = map(int, input().split())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))
able = []
for i in range(N):
    for j in range(M):
        if board[i][j] == 2:
            able.append((i, j))
K = len(able)
used = [0] * K
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
MAX = 0
back(0, [], 'g')
print(MAX)