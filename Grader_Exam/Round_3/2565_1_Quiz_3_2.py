d_student = dict()
d_guest = dict()

n, m, k = [int(e) for e in input().split()]

for i in range(n):
    name, faculty = input().split()
    d_student[name] = faculty

for i in range(m):
    line = input().split()
    guest, name = line[0], line[1:]
    if guest not in d_guest:
        d_guest[guest] = set([d_student[e] for e in name])

for i in range(k):
    line = input().split()
    try:
        sets = [d_guest[e] for e in line]
    except:
        print('None')
        continue
    ans = sets[0]
    for e in sets[1:]:
        ans = set.intersection(ans, e)
    if len(ans) == 0:
        print('None')
    else:
        print(*sorted(ans))