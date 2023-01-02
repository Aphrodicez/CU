d = [0, 3, 6, 9]
suffix = ['', 'K', 'M', 'B']

n = int(input())

if len(str(n)) == 1:
	print(n)
	exit()

s = max(i for i in range(len(d)) if 10 ** d[i] <= n)
ans = str(round(n / (10 ** d[s]), 1)) if len(str(n)) % 3 == 1 and len(str(n)) <= 10 else str(round(n / (10 ** d[s])))

print(ans, suffix[s], sep = '')