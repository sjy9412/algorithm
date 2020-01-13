def move(n, score, marker):
    global MAX
    if n == 10:
        MAX = max(score, MAX)
        return
    for i in range(4):
        if i > 0 and not marker[i - 1]:
            break
        idx = marker[i]
        if idx == 33:
            continue
        elif idx == 5 and dice[n] < 4:
            tmp = 20 + dice[n]
        elif idx == 10 and dice[n] < 3:
            tmp = 23 + dice[n]
        elif idx == 15 and dice[n] < 4:
            tmp = 25 + dice[n]
        elif idx == 5 or idx == 10 or idx == 15:
            if idx == 10:
                tmp = 26 + dice[n]
            else:
                tmp = 25 + dice[n]
        elif 20 < idx < 24 and 29 <= 5 + idx + dice[n] < 33:
            tmp = 5 + idx + dice[n]
        elif 23 < idx < 26 and 29 <= 3 + idx + dice[n] < 33:
            tmp = 3 + idx + dice[n]
        elif (15 < idx < 21 and idx + dice[n] > 20) or  (20 < idx < 24 and 24 <= idx + dice[n]) or (23 < idx < 26 and 26 <= idx + dice[n]) or idx + dice[n] >= 33:
            tmp = 33
        elif idx + dice[n] < 33:
            tmp = idx + dice[n]
        if tmp == 32:
            tmp = 20
        if tmp == 33 or tmp not in marker:
            marker[i] = tmp
            move(n + 1, score + board[tmp], marker)
            marker[i] = idx

dice = list(map(int, input().split()))
MAX = 0
board = [i for i in range(0, 41, 2)] + [13, 16, 19, 22, 24, 28, 27, 26, 25, 30, 35, 0, 0]
move(1, board[dice[0]], [dice[0], 0, 0, 0])
print(MAX)