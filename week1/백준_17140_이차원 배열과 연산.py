r, c, k = map(int, input().split())
A = []
for _ in range(3):
    A.append(list(map(int, input().split())) + [0] * 97)
A += [[0] * 100 for _ in range(97)]
rl = cl = 3
for sec in range(101):
    if A[r - 1][c - 1] == k:
        print(sec)
        break
    if rl >= cl:
        tmp_arr, tmp_l = [], 2
        for i in range(rl):
            nums = dict()
            for j in range(cl):
                num = A[i][j]
                if num and nums.get(num, 0):
                    nums[num] += 1
                elif num:
                    nums[num] = 1
            tmp = [(key, value) for key, value in nums.items()]
            tmp.sort()
            tmp.sort(key = lambda elem: elem[1])
            tmp_arr.append(tmp)
            tmp_l = max(tmp_l, len(tmp) * 2)
        for i in range(rl):
            for j in range(tmp_l):
                if j >= len(tmp_arr[i] * 2):
                    A[i][j] = 0
                elif j % 2:
                    A[i][j] = tmp_arr[i][j // 2][1]
                else:
                    A[i][j] = tmp_arr[i][j // 2][0]
        cl = tmp_l
    else:
        tmp_arr, tmp_l = [], 2
        for i in range(cl):
            nums = dict()
            for j in range(rl):
                num = A[j][i]
                if num and nums.get(num, 0):
                    nums[num] += 1
                elif num:
                    nums[num] = 1
            tmp = [(key, value) for key, value in nums.items()]
            tmp.sort()
            tmp.sort(key=lambda elem: elem[1])
            tmp_arr.append(tmp)
            tmp_l = max(tmp_l, len(tmp) * 2)
        for i in range(cl):
            for j in range(tmp_l):
                if j >= len(tmp_arr[i] * 2):
                    A[j][i] = 0
                elif j % 2:
                    A[j][i] = tmp_arr[i][j // 2][1]
                else:
                    A[j][i] = tmp_arr[i][j // 2][0]
        rl = tmp_l
else:
    print(-1)