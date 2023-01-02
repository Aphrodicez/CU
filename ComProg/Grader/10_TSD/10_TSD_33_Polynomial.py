# coef = coefficient
# deg = degree

def dict2ans(d):
    ans = list()

    for deg in sorted(d.keys(), reverse = True):
        coef = d[deg]
        
        if coef == 0:
            continue
        
        ans.append((coef, deg))

    return ans

def add_poly(p1, p2):
    _sum = dict()
    
    for coef, deg in p1:
        coef, deg = [int(x) for x in [coef, deg]]

        if deg not in _sum:
            _sum[deg] = 0

        _sum[deg] += coef

    for coef, deg in p2:
        coef, deg = [int(x) for x in [coef, deg]]

        if deg not in _sum:
            _sum[deg] = 0

        _sum[deg] += coef

    return dict2ans(_sum)

def mult_poly(p1, p2):
    _prod = dict()

    for (coef_1, deg_1) in p1:
        for (coef_2, deg_2) in p2:
            coef_1, deg_1 = [int(x) for x in [coef_1, deg_1]]
            coef_2, deg_2 = [int(x) for x in [coef_2, deg_2]]

            coef_net = coef_1 * coef_2
            deg_net = deg_1 + deg_2

            if deg_net not in _prod:
                _prod[deg_net] = 0
            
            _prod[deg_net] += coef_net

    return dict2ans(_prod)

# ต้องมีสองคำสั่งข้างล่างนี้ ตอนส่งให้ Grader ตรวจ

for i in range(3):
    exec(input().strip())