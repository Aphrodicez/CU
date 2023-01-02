def convex_polygon_area(p):
    p = p + [p[0]]
    return abs(0.5 * sum(p[i][0] * p[i + 1][1] - p[i][1] * p[i + 1][0] for i in range(len(p) - 1)))

def is_heterogram(s):
    s = ''.join(c for c in s if c.isalpha()).lower()
    return len(s) == len(set(s))

def replace_ignorecase(s, a, b):
    ans = ''
    i = 0
    while i < len(s):
        if s[i : i + len(a)].lower() == a.lower():
            ans += b
            i += len(a)
        else:
            ans += s[i]
            i += 1
    return ans

def top3(votes):
    votes = sorted(votes.items(), key = lambda x : (-x[1], x[0]))
    return [key for key, value in votes[:3]]


# ต้องมีคำสั่งข้างล่างนี้ ตอนส่งให้ Grader ตรวจ
for k in range(2):
    exec(input().strip())