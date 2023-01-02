def cut(s):
	return s[len(s) // 2:] + s[:len(s) // 2]

def slash(s):
	return [[str(s[i // 2]), str(s[len(s) // 2 + i // 2])][i % 2] for i in range(len(s))]

cards = input().split()

for x in input():
	if x not in 'CS':
		continue
	cards = cut(cards) if x == 'C' else slash(cards)

print(*cards)