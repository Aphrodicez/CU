def choose(stu1, stu2):
    ans = [stu1[0], stu2[0]]
    if stu1[2] != 'A' or max(stu1[3:]) > 'C':
        ans.remove(stu1[0])
    if stu2[2] != 'A' or max(stu2[3:]) > 'C':
        ans.remove(stu2[0])
    if len(ans) != 2:
        return ans
    stu1[1] = -float(stu1[1])
    stu2[1] = -float(stu2[1])
    for i in range(1, len(stu1)):
        if stu1[i] == stu2[i]:
            continue
        if stu1[i] < stu2[i]:
            return [stu1[0]]
        return [stu2[0]]
    return [stu1[0], stu2[0]]

exec(input())