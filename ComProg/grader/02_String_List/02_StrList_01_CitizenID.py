s = input()
n12 = (11 - (sum((13 - i) * int(s[i]) for i in range(len(s)))) % 11) % 10
print(s[0], s[1:5], s[5:10], s[10:12], n12)