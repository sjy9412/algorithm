def find():
    for i in range(4):
        num = 0
        for j in range(N // 4):
            t = nums[N // 4 * i + j]
            t = int(t) if t.isdecimal() else trans[t]
            num += t * 16 ** (N // 4 - j - 1)
        tmp.add(num)

trans = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    nums = input()
    tmp = set()
    for _ in range(N // 4):
        nums = nums[-1] + nums[:-1]
        find()
    print('#{}'.format(tc), sorted(list(tmp))[-K])