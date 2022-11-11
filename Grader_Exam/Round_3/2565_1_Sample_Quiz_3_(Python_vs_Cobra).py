votes_in_pak = dict()

n = int(input())
pak_list = []
for i in range(n):
    pak = input().strip()
    pak_list.append(pak)
    votes_in_pak[pak] = list()

pak_of_sorsor = dict()

m = int(input())
for i in range(m):
    name, pak = input().split()
    pak_of_sorsor[name] = pak

q = int(input())

for i in range(q):
    name, vote = input().split()

    votes_in_pak[pak_of_sorsor[name]].append([name, vote])

def check(pak):
    yes = sum(1 for [name, vote] in votes_in_pak[pak] if vote == 'Y')
    no = sum(1 for [name, vote] in votes_in_pak[pak] if vote == 'N')
    xx = sum(1 for [name, vote] in votes_in_pak[pak] if vote == 'X')
    if len([x for x in [yes, no, xx] if x == max([yes, no, xx])]) > 1:
        print('Inconclusive')
        return
    if yes + no + xx == max([yes, no, xx]):
        print('No cobra')
        return
    cobras = []
    if yes == max([yes, no, xx]):
        cobras = [name for [name, vote] in votes_in_pak[pak] if vote != 'Y']
    elif no == max([yes, no, xx]):
        cobras = [name for [name, vote] in votes_in_pak[pak] if vote != 'N']
    else:
        cobras = [name for [name, vote] in votes_in_pak[pak] if vote != 'X']
    cobras = sorted(cobras)
    print(', '.join(cobras))

for pak in pak_list:
    print(pak)
    check(pak)