m, n = map(int, input().split())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
i = j = 0
arr = []
while i < m or j < n:
	if i < m and j < n:
		if arr1[i] <= arr2[j]:
			arr.append(arr1[i])
			i += 1
		else:
			arr.append(arr2[j])
			j += 1
	elif i == m:
		arr += arr2[j:]
		break
	else:
		arr += arr1[i:]
		break
result = ''
for num in arr:
	result += str(num) + ' '
print(result)