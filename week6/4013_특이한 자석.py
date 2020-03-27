from collections import deque

T = int(input())
for tc in range(1, T + 1):
    K = int(input())
    mag = {}
    for i in range(1, 5):
        mag[i] = deque(map(int, input().split()))
    for _ in range(K):
        n, r = map(int, input().split())
        chk = [0] * 5
        chk[n] = r
        for i in range(n, 1, -1):
            if mag[i][-2] != mag[i - 1][2]:
                r *= -1
                chk[i - 1] = r
            else:
                break
        r = chk[n]
        for i in range(n, 4):
            if mag[i][2] != mag[i + 1][-2]:
                r *= -1
                chk[i + 1] = r
            else:
                break
        for i in range(1, 5):
            if chk[i] == 1:
                mag[i].appendleft(mag[i].pop())
            elif chk[i] == -1:
                mag[i].append(mag[i].popleft())
    print('#{}'.format(tc), mag[1][0] + mag[2][0] * 2 + mag[3][0] * 4 + mag[4][0] * 8)