def f1(a, b, c):
    return min(int(x) for x in [a, b, c] if x > 0)

def f2(a, b, c):
    return max(int(x) for x in [a, b, c] if x < 0)

def f3(a, b, c):
    return int(str(abs(sum([a, b, c])))[0])

def f4(a, b, c):
    return int(str(abs(sum([a, b, c])))[-1])

def main():
    s1, s2, a, b, c = [int(e) for e in input().split()]

    if s1 == 0 and s2 == 0:
        print(f1(a, b, c))
    elif s1 == 0 and s2 == 1:
        print(f2(a, b, c))
    elif s1 == 1 and s2 == 0:
        print(f3(a, b, c))
    elif s1 == 1 and s2 == 1:
        print(f4(a, b, c))
    else:
        print('Error')

exec(input().strip()) # DON'T remove this line