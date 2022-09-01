qs = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for i in range(1, len(qs)):
    qs[i] += qs[i - 1]

d = int(input())
m = int(input())
y = int(input()) - 543

print(d + qs[m - 1] + (m > 2) * ((y % 400 == 0) or (y % 100 != 0 and y % 4 == 0)))