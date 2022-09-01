ans = []

n = int(input())

while n != 1:
    ans.append(n)
    n = 3 * n + 1 if n % 2 else n // 2

ans.append(n)

print(*ans[-15:], sep = '->')