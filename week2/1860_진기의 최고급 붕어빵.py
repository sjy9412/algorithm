T = int(input())
for tc in range(1, T + 1):
    N, M, K = map(int, input().split())
    sec = list(map(int, input().split()))
    fish, tmp, result = 0, 0, "Possible"
    sec.sort()
    visit = [0] * (sec[-1] // M + 1)
    for i in range(N):
        idx = sec[i] // M
        if not visit[idx]:
            fish += (idx - tmp) * K
            visit[idx] = 1
            tmp = idx
        if not fish:
            result = "Impossible"
            break
        fish -= 1
    print('#{}'.format(tc), result)