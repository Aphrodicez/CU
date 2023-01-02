qs = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for i in range(1, len(qs)):
    qs[i] += qs[i - 1]

def is_leap_year(y):
    y -= 543
    return (y % 400 == 0) or (y % 100 != 0 and y % 4 == 0)

def day_of_year(d, m, y):
    return d + qs[m - 1] + (m > 2) * is_leap_year(y)

ans = []

while True:
    line = input()
    if line == 'END':
        break
    _id, _type, d, m, y = line.split()
    d, m, y = int(d), int(m), int(y)

    if y < 2558:
        print('Error:', line, '-->', 'Invalid year')
        continue
    if not (1 <= m <= 12):
        print('Error:', line, '-->', 'Invalid month')
        continue
    if not (1 <= d <= (m == 2) * is_leap_year(y) + qs[m] - qs[m - 1]):
        print('Error:', line, '-->', 'Invalid date')
        continue
    if _type not in 'EQNF':
        print('Error:', line, '-->', 'Invalid delivery type')
        continue

    days = day_of_year(d, m, y)
    mp = {'E' : 1, 'Q' : 3, 'N' : 7, 'F' : 14}
    days += mp[_type]
    
    if days > 365 + is_leap_year(y):
        days -= 365 + is_leap_year(y)
        y += 1

    for i in range(1, len(qs)):
        if days <= qs[i] + (i == 2) * is_leap_year(y):
            m = i
            break
    
    d = days - qs[m - 1] - (m > 2) * is_leap_year(y)
    ans.append([_id, d, m, y, day_of_year(d, m, y)])

ans = sorted(ans, key = lambda x : (x[3], x[4], x[0]))

for _id, d, m, y, _ in ans:
    print(_id + ': delivered on ' + '/'.join(map(str, [d, m, y])))