dir = {'N': (-1, 0), 'W': (0, -1), 'E': (0, 1),  'S': (1, 0)}
L = {'N': 'W', 'W': 'S', 'S': 'E', 'E': 'N'}
R = {'N': 'E', 'E': 'S', 'S': 'W', 'W': 'N'}
B, A = map(int, input().split())
N, M = map(int, input().split())
robot = {}
result = 'OK'
board = [[0] * (B + 1) for _ in range(A + 1)]
for i in range(N):
    y, x, d = input().split()
    x = A - int(x) + 1
    y = int(y)
    robot[i + 1] = [(int(x), int(y)), d]
    board[int(x)][int(y)] = i + 1
tmp = []
for _ in range(M):
    tmp.append(input().split())
for num, cmd, cnt in tmp:
    num = int(num)
    if cmd == 'L' or cmd == 'R':
        cnt = int(cnt) % 4
        for _ in range(cnt):
            if cmd == 'L':
                robot[num][1] = L[robot[num][1]]
            else:
                robot[num][1] = R[robot[num][1]]
    else:
        node, d = robot[num]
        x, y = node
        dx, dy = dir[d]
        for _ in range(int(cnt)):
            x, y = x + dx, y + dy
            if 0 < x < A + 1 and 0 < y < B + 1:
                if board[x][y]:
                    result = 'Robot {} crashes into robot {}'.format(num, board[x][y])
                    break
            else:
                result = 'Robot {} crashes into the wall'.format(num)
                break
        else:
            board[node[0]][node[1]] = 0
            board[x][y] = num
            robot[num][0] = (x, y)
    if result != 'OK':
        break
print(result)