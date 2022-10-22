def row_number(t, e): # return row number of t containing e (top row is row #0)
    for i in range(len(t)):
        if e in t[i]: 
            return i

def flatten(t): # return a list of ints converted from list of lists of ints t
    ans = []
    for x in t:
        ans += x
    ans.remove(0)
    return ans

def inversions(x): # return the number of inversions of list x
    cnt = 0
    for i in range(len(x)):
        for j in range(i + 1, len(x)):
            if x[i] > x[j]:
                cnt += 1
    return cnt

def solvable(t): 
    # return True if tiling t (list of lists of ints) is solvable
    # otherwise return False
    cnt_row = len(t)
    cnt_inversions = inversions(flatten(t))
    zero_row = row_number(t, 0)
    if cnt_row % 2 == 1 and cnt_inversions % 2 == 0:
            return True
    if cnt_row % 2 == 0 and (cnt_inversions % 2 != zero_row % 2):
            return True
    return False

exec(input().strip()) # do not remove this line