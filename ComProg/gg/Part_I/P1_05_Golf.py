pars, stroke, repair = [0] * 9, [0] * 9, [0] * 9

for i in range(9):
    pars[i], stroke[i], c = map(int, input().split())
    repair[i] = 0 if not c else min(pars[i] + 2, stroke[i])
    
handicap = 0.8 * (1.5 * sum(repair) - sum(pars))
handicap = int(handicap) if handicap >= 0 else -(int(-handicap) + 1)

print(sum(stroke))
print(handicap)
print(sum(stroke) - handicap)