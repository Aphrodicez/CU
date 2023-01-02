n = int(input())

winner = set()
loser = set()

for i in range(n):
    w, l = input().split()
    winner.add(w)
    loser.add(l)

print(sorted(list(set.difference(winner, loser))))