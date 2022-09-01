def dis(x, y):
	return ((x * x) + (y * y)) ** 0.5

a = []

n = int(input())

for i in range(n):
	x, y = map(float, input().split())
	a.append((x, y, i + 1))

a = sorted(a, key = lambda x : dis(x[0], x[1]))

print('#%d:' % (a[2][2]), a[2][:2])