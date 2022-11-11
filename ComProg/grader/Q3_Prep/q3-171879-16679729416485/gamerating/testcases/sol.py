d_score = dict()
d_level = dict()
d_rating = dict()

sum_rating = 0

n = int(input())

for i in range(n):
    line = input().split(' | ')
    opr = line[0]
    if opr == 'Play':
        name = line[1]
        level = int(line[2])
        score = int(line[3])
        d_level[name] = level
        d_score[name] = score
        d_rating[name] = max(d_rating.get(name, 0), (25 * (d_level[name] + 1) * d_score[name]) // 10**7)
    elif opr == 'Rating':
        if len(line) == 1:
            print(sum(sorted(d_rating.values(), reverse = True)[:5]))
            continue
        name = line[1]
        print(d_rating.get(name, 0))
    elif opr == 'Detail':
        name = line[1]
        if name not in d_rating:
            print(('%s: No play history') % name)
            continue
        print(name, d_level[name], d_score[name], d_rating[name], sep = ' | ')