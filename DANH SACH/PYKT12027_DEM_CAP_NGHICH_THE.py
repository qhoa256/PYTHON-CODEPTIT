def mergeSort(a, n):
	tmp_a = [0] * n
	return _mergeSort(a, tmp_a, 0, n-1)

def _mergeSort(a, tmp_a, l, r):
	cnt = 0
	if l < r:
		m = (l + r)//2
		cnt += _mergeSort(a, tmp_a, l, m)
		cnt += _mergeSort(a, tmp_a, m + 1, r)
		cnt += merge(a, tmp_a, l, m, r)
	return cnt

def merge(a, tmp_a, l, m, r):
	i = l	 
	j = m + 1 
	k = l	 
	cnt = 0
	while i <= m and j <= r:
		if a[i] <= a[j]:
			tmp_a[k] = a[i]
			k += 1
			i += 1
		else:
			tmp_a[k] = a[j]
			cnt += (m - i + 1)
			k += 1
			j += 1
	while i <= m:
		tmp_a[k] = a[i]
		k += 1
		i += 1
	while j <= r:
		tmp_a[k] = a[j]
		k += 1
		j += 1
	for i in range(l, r + 1):
		a[i] = tmp_a[i]
	return cnt

if __name__ == "__main__":
	n = int(input())
	a = list(map(int, input().split()))
	print(mergeSort(a, n))