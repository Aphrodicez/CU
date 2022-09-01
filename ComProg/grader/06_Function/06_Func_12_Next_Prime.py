def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def next_prime(N):
    i = N + 1
    while True:
        if is_prime(i):
            return i
        i += 1
  
def next_twin_prime(N):
    i = N + 1
    while True:
        if is_prime(i) and is_prime(i + 2):
            return (i, i + 2)
        i += 1

exec(input().strip())