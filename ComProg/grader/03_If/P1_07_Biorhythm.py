from math import pi
from math import sin

qs = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for i in range(1, len(qs)):
    qs[i] += qs[i - 1]

def is_leap_year(y):
    return (y % 400 == 0) or (y % 100 != 0 and y % 4 == 0)

def day_of_year(d, m, y):
    return d + qs[m - 1] + (m > 2) * is_leap_year(y)

bd, bm, by, d, m, y = [int(x) for x in input().split()]
by -= 543
y -= 543

t = 0
t += (365 + is_leap_year(by)) - (day_of_year(bd, bm, by) - 1)
t += day_of_year(d, m, y) - 1
t += 365 * max(0, y - by - 1)

c = 2 * pi * t
print(t, '{:.2f}'.format(sin(c / 23)), '{:.2f}'.format(sin(c / 28)), '{:.2f}'.format(sin(c / 33)))