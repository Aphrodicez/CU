d = dict()

n = int(input())
for i in range(n):
    team, nation = input().split()
    d[team] = nation

while True:
    line = input().split()
    if line[0] == 'q':
        break
    try:
        line = [d[x] for x in line]
    except:
        print('Not OK')
        continue
    if len(set(line)) != len(line):
        print('Not OK')
        continue
    print('OK')