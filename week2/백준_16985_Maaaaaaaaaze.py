def back(choice):
    if MIN == 13:
        return
    if len(choice) == 5:
        dir([], choice)
        return
    for i in range(5):
        if not choice and i == 4:
            continue
        elif 0 < len(choice) < 4 and choice[0] == 3 and i == 4:
            continue
        elif (len(choice) == 2 and sum(choice) + i == 9 or len(choice) == 3 and sum(choice) != 3 and i > 2) and choice[0] == 2:
            continue
        elif len(choice) == 3 and choice[0] == 1 and sum(choice) + i == 10:
            continue
        if not used[i]:
            used[i] = 1
            choice.append(i)
            back(choice)
            choice.pop()
            used[i] = 0

def dir(choice, num):
    global MIN
    if MIN == 13:
        return
    if len(choice) == 1 and not rot[choice[0]][num[0]][0][0]:
        return
    if len(choice) == 5:
        if not rot[choice[4]][num[4]][4][4]:
            return
        maze = [[[0] * 5 for _ in range(5)] for _ in range(5)]
        visit = [[[0] * 5 for _ in range(5)] for _ in range(5)]
        for j in range(5):
            for x in range(5):
                for y in range(5):
                    maze[j][x][y] = rot[choice[j]][num[j]][x][y]
        tmp = [(0, 0, 0)]
        visit[0][0][0] = 1
        while tmp:
            x, y, z = tmp.pop(0)
            if visit[x][y][z] >= MIN:
                break
            if (x, y, z) == (4, 4, 4):
                MIN = min(MIN, visit[4][4][4])
                if MIN == 13:
                    return
                break
            for d in range(6):
                tx, ty, tz = x + dx[d], y + dy[d], z + dz[d]
                if -1 < tx < 5 and -1 < ty < 5 and -1 < tz < 5 and maze[tx][ty][tz] and not visit[tx][ty][tz]:
                    visit[tx][ty][tz] = visit[x][y][z] + 1
                    tmp.append((tx, ty, tz))
        return
    for i in range(4):
        choice.append(i)
        dir(choice, num)
        choice.pop()

def rot_arr(n, b1, b2):
    for i in range(5):
        for j in range(5):
            for k in range(5):
                b2[i][j][k] = b1[i][k][4 - j]
    rot[n] = b2

board = [[] for _ in range(5)]
for i in range(5):
    for _ in range(5):
        board[i].append(list(map(int, input().split())))
used = [0] * 5
dx, dy, dz = [1, -1, 0, 0, 0, 0], [0, 0, 1, -1, 0, 0], [0, 0, 0, 0, 1, -1]
MIN = 0xffff
number = []
rot = {0: board}
rot_arr(1, board, [[[0] * 5 for _ in range(5)] for _ in range(5)])
rot_arr(2, rot[1], [[[0] * 5 for _ in range(5)] for _ in range(5)])
rot_arr(3, rot[2], [[[0] * 5 for _ in range(5)] for _ in range(5)])
back([])
print(-1 if MIN == 0xffff else MIN - 1)