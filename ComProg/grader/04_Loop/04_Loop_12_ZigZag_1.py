line = [[], []]

n = int(input())

for i in range(n):
    x, y = map(int, input().split())
    line[i % 2].append(x)
    line[1 - i % 2].append(y)
opr = input()

if opr == 'Zig-Zag':
    print(min(line[0]), max(line[1]))
if opr == 'Zag-Zig':
    print(min(line[1]), max(line[0]))