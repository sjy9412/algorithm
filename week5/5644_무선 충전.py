def find(Ax, Ay, Bx, By):
    MAX = 0
    if not board[Ax][Ay]:
        for b in board[Bx][By]:
            MAX = max(MAX, charge[b])
    elif not board[Bx][By]:
        for a in board[Ax][Ay]:
            MAX = max(MAX, charge[a])
    for a in board[Ax][Ay]:
        for b in board[Bx][By]:
            if a == b:
                MAX = max(MAX, charge[a])
            else:
                MAX = max(MAX, charge[a] + charge[b])
    return MAX


T = int(input())
dir = {0: (0, 0), 1: (-1, 0), 2: (0, 1), 3: (1, 0), 4: (0, -1)}
for tc in range(1, T + 1):
    M, A = map(int, input().split())
    board = [[[]for _ in range(11)] for _ in range(11)]
    result = 0
    node = [1, 1, 10, 10]
    move_A = list(map(int, input().split()))
    move_B = list(map(int, input().split()))
    charge = {}
    for num in range(A):
        y, x, c, p = map(int, input().split())
        charge[num] = p
        for i in range(1, 11):
            for j in range(1, 11):
                if abs(x - i) + abs(y - j) <= c:
                    board[i][j].append(num)
    result += find(1, 1, 10, 10)
    for s in range(M):
        Adx, Ady = dir[move_A[s]]
        Bdx, Bdy = dir[move_B[s]]
        node[0] += Adx
        node[1] += Ady
        node[2] += Bdx
        node[3] += Bdy
        Ax, Ay, Bx, By = node
        result += find(Ax, Ay, Bx, By)
    print('#{}'.format(tc), result)