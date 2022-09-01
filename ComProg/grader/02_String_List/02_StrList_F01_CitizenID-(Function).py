def check_digit(s):
    return (11 - (sum((13 - i) * int(s[i]) for i in range(len(s)))) % 11) % 10

exec(input())