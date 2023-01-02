s = input()

ans = [str(i) for i in range(10) if str(i) not in s]

print(','.join(ans) if len(ans) else 'None')