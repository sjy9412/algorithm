T = int(input())
for tc in range(1, T + 1):
    N, M, K = map(int, input().split())
    sec = list(map(int, input().split()))
    fish, chk, result = 0, False, "Possible"
    sec.sort()
    for s in range(max(sec) + 1):
        if s and not s % M:
            fish += K
        while sec and s == sec[0]:
            if not fish:
                result = "Impossible"
                break
            sec.pop(0)
            fish -= 1
        if result == "Impossible":
            break
    print('#{}'.format(tc), result)