from queue import PriorityQueue

def MST(s):
    visit = [0] * l
    key = [0xffff] * l
    Q = PriorityQueue()
    Q.put((0, s))
    key[0] = 0
    while not Q.empty():
        d, u = Q.get()
        visit[u] = 1
        for i in range(len(node[u])):
            x, y = node[u][i][0], node[u][i][1]
            for k in range(4):
                cnt = 0
                tx, ty = x + dx[k], y + dy[k]
                while -1 < tx < N and -1 < ty < M:
                    if board[tx][ty]:
                        if key[board[tx][ty] - 2] > cnt > 1 and not visit[board[tx][ty] - 2]:
                            key[board[tx][ty] - 2] = cnt
                            Q.put((cnt, board[tx][ty] - 2))
                        break
                    tx += dx[k]
                    ty += dy[k]
                    cnt += 1
    return sum(key) if sum(visit) == l else -1

N, M = map(int, input().split())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
node, l = [[] for _ in range(6)], 0
for i in range(N):
    for j in range(M):
        if board[i][j] == 1:
            tmp = [(i, j)]
            l += 1
            node[l - 1].append((i, j))
            board[i][j] += l
            while tmp:
                x, y = tmp.pop()
                for k in range(4):
                    tx, ty = x + dx[k], y + dy[k]
                    if -1 < tx < N and -1 < ty < M and board[tx][ty] == 1:
                        tmp.append((tx, ty))
                        node[l - 1].append((tx, ty))
                        board[tx][ty] += l
print(MST(0))