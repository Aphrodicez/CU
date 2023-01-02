def make_int_list(s):
    return [int(x) for x in s.split()]

def is_odd(e):
    return bool(e % 2)

def odd_list(alist):
    return [x for x in alist if is_odd(x)]

def sum_square(alist):
    return sum([x * x for x in alist])

exec(input().strip())