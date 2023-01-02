offset, id = 0, 0
q = []
qtime = []

query = []

n = int(input())
for i in range(n):
    s = input()
    try:
        opr, val = s.split()
    except:
        opr, val = s, 0
    val = int(val)
    query.append([opr, val])

for i in range(n):
    opr, val = query[i]
    if opr == 'reset':
        offset = val
    if opr == 'new':
        print('ticket', offset + id)
        q.append([offset + id, val])
        id += 1
    if opr == 'next':
        print('call', q[0][0])
        if i + 1 < len(query) and query[i + 1][0] != 'order':
            q.pop(0)
    if opr == 'order':
        print('qtime', q[0][0], val - q[0][1])
        qtime.append(val - q[0][1])
        q.pop(0)
    if opr == 'avg_qtime':
        print('avg_qtime', round(sum(qtime) / len(qtime), 4))
    lastopr = opr