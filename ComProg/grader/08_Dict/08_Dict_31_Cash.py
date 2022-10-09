def total(pocket):
    return sum([key * value for key, value in pocket.items()])

def take(pocket, money_in):
    for key, value in money_in.items():
        if key not in pocket.keys():
            pocket[key] = 0
        pocket[key] += value
 
def pay(pocket, amt):
    if total(pocket) - amt < 0:
        return {}
    pay_dict = {}
    for key in sorted(pocket.keys())[::-1]:
        if amt == 0:
            break
        cnt = min(pocket[key], amt // key)
        if cnt == 0:
            continue
        pocket[key] -= cnt
        pay_dict[key] = cnt
        amt -= key * cnt
    return pay_dict

exec(input().strip()) # ต้องมีคำสั่งนี้ ตรงนี้ตอนส่ง ให้เกรดเดอร์ตรวจ