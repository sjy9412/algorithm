dir = {'U': (-1, 0), 'R': (0, 1), 'D': (1, 0), 'L': (0, -1)}
dir1 = {(-1, 0): (0, -1), (0, -1): (-1, 0), (0, 1): (1, 0), (1, 0): (0, 1)}
dir2 = {(0, 1): (-1, 0), (0, -1): (1, 0), (1, 0): (0, -1), (-1, 0): (0, 1)}
N, M = map(int, input().split())
board = []
for _ in range(N):
    board.append(list(input()))
PR, PC = map(int, input().split())
result_d = ''
result = 0
for d in 'URDL':
    cnt = 0
    dx, dy = dir[d]
    x, y = PR - 1, PC - 1
    while result != "Voyager":
        x, y = x + dx, y + dy
        cnt += 1
        if cnt > M * N:
            result_d = d
            result = "Voyager"
            break
        if -1 < x < N and -1 < y < M and board[x][y] != 'C':
            if board[x][y] == '\\':
                dx, dy = dir1[(dx, dy)]
            elif board[x][y] == '/':
                dx, dy = dir2[(dx, dy)]
        else:
            if result < cnt:
                result_d = d
                result = cnt
            break
print(result_d)
print(result)