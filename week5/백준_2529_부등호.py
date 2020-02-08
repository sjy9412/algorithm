def back(num):
    global MIN, MAX
    i = len(num)
    if i == k + 1:
        print(num)
        MAX = max(MAX, num)
        MIN = min(MIN, num)
        return
    for n in range(10):
        if not used[n] and (i == 0 or (i > 0 and ine[i - 1] == '<' and int(num[-1]) < n) or (i > 0 and ine[i - 1] == '>' and int(num[-1]) > n)):
            used[n] = 1
            back(num + str(n))
            used[n] = 0


k = int(input())
ine = input().split()
MIN, MAX = str(9999999999), str(0)
used = [0] * 10
back('')
print(MAX)
print(MIN)
