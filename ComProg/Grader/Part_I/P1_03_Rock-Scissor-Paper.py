p1w = [['R', 'S'], ['P', 'R'], ['S', 'P']]
p2w = [[y, x] for [x, y] in p1w]

p1 = p2 = 0
i = 0

m = int(input())

while True:
	try:
		s = input().split()
	except:
		break
	p1 += s in p1w
	p2 += s in p2w
	i += 1
	if max(p1, p2) == m or i == 3 * m:
		break

print(p1, p2)

if p1 == p2:
	print('Tie')
	exit()

print('Player %d wins' % ((p2 > p1) + 1))