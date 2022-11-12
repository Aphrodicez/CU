d_ally = dict()
d_enemy = dict()

def is_enemy(u, v):
    d_ally[u] = set.union(d_ally.get(u, set()), set([u]))
    d_ally[v] = set.union(d_ally.get(v, set()), set([v]))
    enemy_v = d_enemy.get(u, set())
    
    for ally in d_ally.get(v, set()):
        enemy_v = set.union(enemy_v, d_enemy.get(ally, set()))

    return (len(set.intersection(d_ally.get(u, set()), enemy_v)) != 0)

while True:
    line = input().split()
    if line[0] == 'End':
        break

    opr, nations = line[0], line[1:]

    if opr == 'Ally':
        for nation in nations:
            d_ally[nation] = set(nations)

    if opr == 'Enemy':
        for nation in nations:
            d_enemy[nation] = set.union(d_enemy.get(nation, set()), set.difference(set(nations), set([nation])))

    if opr == 'Table':
        ch = True
        for i in range(len(nations)):
            if is_enemy(nations[i], nations[(i + 1) % len(nations)]):
                ch = False
                break

        print('Okay' if ch else 'No')