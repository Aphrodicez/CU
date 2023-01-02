def grade_mcq(sol, ans):
    if len(sol) != len(ans):
        return -1
    return sum(sol[i] == ans[i] for i in range(len(sol)))

exec(input())