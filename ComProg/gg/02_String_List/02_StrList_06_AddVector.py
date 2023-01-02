a = [float(x) for x in input().strip('[]').split(', ')]
b = [float(x) for x in input().strip('[]').split(', ')]

print(a, '+', b, '=', [a[i] + b[i] for i in range(len(a))])