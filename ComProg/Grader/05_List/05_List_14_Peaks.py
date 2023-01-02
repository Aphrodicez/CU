s = [int(x) for x in input().split()]
print(sum((s[i] > max(s[i - 1], s[i + 1])) for i in range(1, len(s) - 1)))