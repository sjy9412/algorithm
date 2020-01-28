from queue import PriorityQueue

def MST(s):
    visit = [0] * l
    key = [0xffff] * l
    Q = PriorityQueue()
    Q.put((0, s))
    key[0] = 0
    for _ in range(l):
        d, u = Q.get()
        print((d, u))
        visit[u] = 1
        for i in range(len(node[u])):
            x, y = node[u][i]
            print(x, y)
            for k in range(4):
                cnt = 0
                tx, ty = x + dx[k], y + dy[k]
                while -1 < tx < N and -1 < ty < M:
                    idx = board[tx][ty]
                    if idx:
                        if key[idx - 2] > cnt > 1 and not visit[idx - 2]:
                            key[idx - 2] = cnt
                            Q.put((cnt, idx - 2))
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