def sqrt_n_times(x, n):
    for i in range(n):
        x = x ** 0.5
    return x

def cube_root(y):
    y = sqrt_n_times(y, 2)
    for i in range(1, 8 + 1):
        y = y * (sqrt_n_times(y, 2 ** i))
    return y

def main():
    q = float(input())
    print(cube_root(q))

exec(input())