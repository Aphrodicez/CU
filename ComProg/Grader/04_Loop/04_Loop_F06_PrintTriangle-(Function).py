def print_triangle(h):
    for i in range(1, h):
        s = ' ' * (h - i)
        for j in range(1, 2 * i):
            s += '*' if j == 1 or j == 2 * i - 1 else ' '
        print(s)
    print('*' * (2 * h - 1))

exec(input())