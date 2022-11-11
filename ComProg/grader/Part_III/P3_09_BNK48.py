scores = dict()
cnt_ota = dict()
vote_for = dict()
kami = dict()

while True:
    line = input()
    if len(line) == 1:
        break
    ota, member, point = line.split()
    
    if member not in scores:
        scores[member] = 0
    scores[member] += int(point)

    if member not in cnt_ota:
        cnt_ota[member] = set()
    cnt_ota[member].add(ota)

    if ota not in vote_for:
        vote_for[ota] = dict()
    if member not in vote_for[ota]:
        vote_for[ota][member] = 0
    
    vote_for[ota][member] += int(point)

opr = int(line)

ans = []

if opr == 1:
    ans = list(scores.items())
    ans = sorted(ans, key = lambda x : (-x[1], x[0]))

if opr == 2:
    ans = [[x, len(cnt_ota[x])] for x in cnt_ota.keys()]
    ans = sorted(ans, key = lambda x : (-x[1], x[0]))

if opr == 3:
    for ota in vote_for.keys():
        kami_rank = list(vote_for[ota].items())
        this_kami = sorted(kami_rank, key = lambda x : (-x[1], x[0]))[0][0]
        kami[this_kami] = kami.get(this_kami, 0) + 1
    for member in scores.keys():
        kami[member] = kami.get(member, 0)
    
    ans = list(kami.items())
    ans = sorted(ans, key = lambda x : (-x[1], x[0]))

print(', '.join([x[0] for x in ans][:3]))