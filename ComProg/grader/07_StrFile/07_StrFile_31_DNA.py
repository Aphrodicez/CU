d = {
    'A' : 'T',
    'T' : 'A',
    'G' : 'C',
    'C' : 'G'
}

dna = 'ATGC'

s = input().strip().upper()
opr = input().strip()

if any(x not in dna for x in s):
    print('Invalid DNA')

elif opr == 'R':
    print(''.join([d[x] for x in s])[::-1])

elif opr == 'F':
    print(', '.join([str(x) + '=' + str(s.count(x)) for x in dna]))

elif opr == 'D':
    substr = input().strip()
    print(sum(s[i : i + 2] == substr for i in range(len(s) - 1)))