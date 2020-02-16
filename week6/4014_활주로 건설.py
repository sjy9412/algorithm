T = int(input())
for tc in range(1, T + 1):
    N, X = map(int, input().split())
    board = []
    for _ in range(N):
        board.append(list(map(int, input().split())))
    result = 0
    for i in range(N):
        x, l = 0, 1
        for j in range(1, N):
            tmp = board[i][j - 1]
            h = board[i][j]
            if h == tmp - 1:
                if 0 < x < X:
                    break
                else:
                    x = l = 1
            elif h == tmp + 1:
                if 0 < x < X or l < X:
                    break
                else:
                    x, l = 0, 1
            elif h == tmp and x:
                x += 1
                if x == X:
                    x = l = 0
            elif h == tmp:
                l += 1
            else:
                break
        else:
            if x == 0:
                result += 1
        x, l = 0, 1
        for j in range(1, N):
            tmp = board[j - 1][i]
            h = board[j][i]
            if h == tmp - 1:
                if 0 < x < X:
                    break
                else:
                    x = l = 1
            elif h == tmp + 1:
                if 0 < x < X or l < X:
                    break
                else:
                    x, l = 0, 1
            elif h == tmp and x:
                x += 1
                if x == X:
                    x = l = 0
            elif h == tmp:
                l += 1
            else:
                break
        else:
            if x == 0:
                result += 1
    print('#{}'.format(tc), result)