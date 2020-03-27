def stick(i, j, sticker):
    tmp = []
    cnt = 0
    for x in range(len(sticker)):
        for y in range(len(sticker[0])):
            if sticker[x][y] and board[i + x][j + y] == 0:
                tmp.append((i + x, j + y))
                cnt += 1
            elif sticker[x][y]:
                return 0
    for x, y in tmp:
        board[x][y] = 1
    return cnt

def turn(sticker):
    tmp = [[0] * len(sticker) for _ in range(len(sticker[0]))]
    X, Y = len(sticker), len(sticker[0])
    for x in range(X):
        for y in range(Y):
            tmp[y][x] = sticker[X - 1 - x][y]
    return tmp

N, M, K = map(int, input().split())
board = [[0] * M for _ in range(N)]
result = 0
for _ in range(K):
    R, C = map(int, input().split())
    sticker = []
    cnt = 0
    for _ in range(R):
        line = list(map(int, input().split()))
        cnt += line.count(1)
        sticker.append(line)
    if cnt > N * M - result:
        continue
    flag = False
    for t in range(4):
        for i in range(N - len(sticker) + 1):
            for j in range(M - len(sticker[0]) + 1):
                if board[i][j] and sticker[0][0]:
                    continue
                tmp = stick(i, j, sticker)
                if tmp:
                    result += tmp
                    flag = True
                    break
            if flag:
                break
        if flag:
            break
        elif t < 3:
            sticker = turn(sticker)
print(result)