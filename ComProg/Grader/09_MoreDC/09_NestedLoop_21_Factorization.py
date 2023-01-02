def isPrime(n):
    if n <= 1:
        return False

    sq = int(n ** 0.5)
    
    for i in range(2, sq + 1):
        if n % i == 0:
            return False
    return True

def factor(N):
    f = []
    sq = int(N ** 0.5)
    for i in range(2, sq + 1):
        if not isPrime(i):
            continue
        cnt = 0
        while N % i == 0:
            N //= i
            cnt += 1
        if cnt == 0:
            continue
        f.append([i, cnt])
    
    if N != 1:
        f.append([N, 1])
    if len(f) == 0:
        return []
    return f

exec(input().strip()) # ต้องมีคำสั่งนี้ ตรงนี้ ตอนส่งให้ Grader ตรวจ