s = ''
opr = input()
row = int(input())

ans = []
for i in range(row):
    ans += [input()]
    s += ans[i]

if min(len(x) for x in ans) != max(len(x) for x in ans):
    print('Invalid size')
    exit()

col = len(s) // row

if opr == '90':
    ans = []
    st = (row - 1) * col
    while st != row * col:
        ans += [''.join(s[i] for i in range(st, -1, -col))]
        st += 1

if opr == '180':
    ans = [x[::-1] for x in ans[::-1]]

if opr == 'flip':
    ans = [x[::-1] for x in ans]

print(*ans, sep = '\n')