x1 = input().strip()
x2 = input().strip()
x3 = input().strip()

x = x1 + x2 + x3
if len(x) == 9:
    win = "-"
    i = 0
    while i < 3:
        if len(set(x[3 * i : 3 * i + 3])) == 1:
            win = x[3 * i]
            break
        if x[i] == x[i + 3] == x[i + 6]:
            win = x[i]
            break
        i += 1
    if win == '-':
        if x[0] == x[4] == x[8]:
            win = x[0]
        if x[3] == x[4] == x[6]:
            win = x[6]
    if win == '-':
        print('???')
    else:
        print(win)
else:
    print('ERROR')