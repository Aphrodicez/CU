a = ['zero', 'positive', 'negative']

n = int(input())

print(a[n // max(1, abs(n))], 'odd' if n % 2 else 'even')