d_name = dict()
d_money = dict()

def transaction(name, account, opr, money):
    if opr not in ['withdraw', 'deposit']:
        return True
    if account not in d_name:
        if opr == 'withdraw':
            print('Transaction Failed')
            return False
        else:
            d_name[account] = name
            d_money[account] = 0
    if d_name[account] != name:
        print('Transaction Failed')
        return False
    if opr == 'deposit':
        d_money[account] += money
    if opr == 'withdraw':
        if d_money[account] - money < 0:
            print('Transaction Failed')
            return False
        d_money[account] -= money
    
    money_net = d_money[account]
    if money_net == int(money_net):
        money_net = int(money_net)
    
    print(name, '(' + account + ')', money_net)
    return True

n = int(input())
for i in range(n):
    name, account, money = [x.strip() for x in input().split()]
    money = float(money)
    d_name[account] = name
    d_money[account] = money

while True:
    line = [x.strip() for x in input().split()]
    if len(line) == 1:
        break
    if len(line) == 4:
        name, account, opr, money = line
        money = float(money)
        if not transaction(name, account, opr, money):
            continue
    else:
        name, account, opr, o_account, money = line
        money = float(money)
        if not transaction(name, account, 'withdraw', money):
            continue
        transaction(d_name[o_account], o_account, 'deposit', money)