def back(s, choice):
    global MIN
    s1, s2 = [], []
    for i in range(len(people)):
        if i in choice:
            s1.append(d1[i])
        else:
            s2.append(d2[i])
    MIN = min(MIN, max(move(s1, stair[0][0]), move(s2, stair[1][0])))
    for k in range(s, len(people)):
        choice.append(k)
        back(k + 1, choice)
        choice.pop()


def move(s, t):
    s.sort()
    if not s:
        return 0
    go = []
    wait = []
    for _ in range(len(s)):
        d = s.pop(0)
        if d > MIN:
            return 100
        for _ in range(len(go)):
            if go[0] - d < 1:
                tmp = go.pop(0)
                if wait:
                    go.append(tmp + wait.pop(0))
        if len(go) < 3:
            go.append(d + t + 1)
        else:
            wait.append(t)
    return go[-1] if not wait else go[len(wait) % 3 - 1] + ((len(wait) - 1) // 3 + 1) * t


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    people = []
    stair = []
    d1, d2 = [], []
    MIN = 100
    for i in range(0, N):
        tmp = list(map(int, input().split()))
        for j in range(N):
            if tmp[j] == 1:
                people.append((i, j))
            elif tmp[j]:
                stair.append((tmp[j], i, j))
    for x, y in people:
        d1.append(abs(x - stair[0][1]) + abs(y - stair[0][2]))
        d2.append(abs(x - stair[1][1]) + abs(y - stair[1][2]))
    back(0, [])
    print('#{}'.format(tc), MIN)