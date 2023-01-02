qs = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for i in range(1, len(qs)):
    qs[i] += qs[i - 1]

def is_leap_year(y):
    y -= 543
    return (y % 400 == 0) or (y % 100 != 0 and y % 4 == 0)

def day_of_year(d, m, y):
    return d + qs[m - 1] + (m > 2) * is_leap_year(y)

exec(input())