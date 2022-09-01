name = ['Robert', 'William', 'James', 'John', 'Margaret', 'Edward', 'Sarah', 'Andrew', 'Anthony', 'Deborah']
nickname = ['Dick', 'Bill', 'Jim', 'Jack', 'Peggy', 'Ed', 'Sally', 'Andy', 'Tony', 'Debbie']

n = int(input())

for i in range(n):
    s = input()
    if s in name:
        print(nickname[name.index(s)])
    elif s in nickname:
        print(name[nickname.index(s)])
    else:
        print('Not found')