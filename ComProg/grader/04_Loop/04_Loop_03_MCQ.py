sol = input()
sub = input()

if len(sol) != len(sub):
    print('Incomplete answer')
    exit()
    
print(sum(sol[i] == sub[i] for i in range(len(sol))))