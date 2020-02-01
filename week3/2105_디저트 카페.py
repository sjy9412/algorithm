def find(x, y, n, k):
    visit = {board[x][y]}
    for _ in range(k):
        tx, ty = x + 1, y + 1
        if not (-1 < tx < N) or not (-1 < ty < N) or board[tx][ty] in visit:
            return 0
        x, y = tx, ty
        visit.add(board[x][y])
    for _ in range(n - k):
        tx, ty = x + 1, y - 1
        if not (-1 < tx < N) or not (-1 < ty < N) or board[tx][ty] in visit:
            return 0
        x, y = tx, ty
        visit.add(board[x][y])
    for _ in range(k):
        tx, ty = x - 1, y - 1
        if not (-1 < tx < N) or not (-1 < ty < N) or board[tx][ty] in visit:
            return 0
        x, y = tx, ty
        visit.add(board[x][y])
    for _ in range(n - k - 1):
        tx, ty = x - 1, y + 1
        if not (-1 < tx < N) or not (-1 < ty < N) or board[tx][ty] in visit:
            return 0
        x, y = tx, ty
        visit.add(board[x][y])
    return n

def dessert():
    result = 0
    for i in range(N - 2):
        for j in range(1, N - 1):
            for n in range(N - i - 1, 1, -1):
                for k in range(1, n):
                    tmp = find(i, j, n, k)
                    if tmp and tmp == N - i - 1:
                        return tmp * 2
                    elif tmp:
                        result = max(result, tmp* 2)
        if result >= (N - i - 1) * 2:
            return result
    return -1

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    board = []
    for _ in range(N):
        board.append(list(map(int, input().split())))
    print('#{}'.format(tc), dessert())