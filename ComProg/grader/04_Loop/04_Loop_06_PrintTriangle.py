n = int(input())

for i in range(1, n):
	s = ' ' * (n - i)
	for j in range(2 * i - 1):
		if j == 0 or j == 2 * i - 2:
			s += '*'
		else:
			s += ' '
	print(s)

print('*' * (2 * n - 1))