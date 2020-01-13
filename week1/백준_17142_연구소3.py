from collections import deque

# 백트레킹으로 바이러스를 M개 선택
def back(n, idx):
    global MIN, room
    if n == M:
        tmp, cnt, sec = deque(), 0, 0
        # set에 넣어서 visit 체크해주는 것보다 visit 배열로 체크하는게 더 빠름
        visit = [[0] * N for _ in range(N)]
        # bfs로 바이러스가 퍼질 수 있는지 확인
        for i in range(M):
            tmp.append(virus[choice[i]])
        while tmp:
            sec += 1
            if sec >= MIN:
                return
            for _ in range(len(tmp)):
                x, y = tmp.popleft()
                for k in range(4):
                    tx, ty = x + dx[k], y + dy[k]
                    if -1 < tx < N and -1 < ty < N and board[tx][ty] != 1 and not visit[tx][ty]:
                        tmp.append((tx, ty))
                        visit[tx][ty] = 1
                        # cnt에 바이러스가 퍼진 방 개수 세기
                        if not board[tx][ty]:
                            cnt += 1
            # 빈 방의 개수와 바이러스가 퍼진 방 개수가 같으면 return
            if room == cnt:
                MIN = min(MIN, sec)
                return
        return
    for i in range(idx, len(virus)):
        choice[n] = i
        back(n + 1, i + 1)

N, M = map(int, input().split())
board = []
virus, room, MIN = [], 0, 2500
choice = [0] * M
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
for _ in range(N):
    board.append(list(map(int, input().split())))
# 바이러스가 있으면 vurus에 추가
# 바이러스가 퍼질 수 있는 방 개수
for i in range(N):
    for j in range(N):
        if board[i][j] == 2:
            virus.append((i, j))
        if not board[i][j]:
            room += 1
if room:
    back(0, 0)
else:
    MIN = 0
print(-1 if MIN == 2500 else MIN)