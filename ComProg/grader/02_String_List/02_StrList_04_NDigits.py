m = input()
n = int(input())

print(('0' * n + m)[-max(n, len(m)) : ])