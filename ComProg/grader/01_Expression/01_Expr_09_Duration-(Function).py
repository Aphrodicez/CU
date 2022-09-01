def str2hms(hms_str):
    t = hms_str.split(':')
    return int(t[0]), int(t[1]), int(t[2])

def hms2str(h, m, s):
    return ':'.join([('0' + str(x))[-2:] for x in [h, m, s]])

def to_sec(h, m, s):
    return h * 3600 + m * 60 + s

def to_hms(s):
    h, m, s = s // 3600, (s // 60) % 60, s % 60
    return h, m, s

def diff(h1, m1, s1, h2, m2, s2):
    return to_hms(to_sec(h2, m2, s2) - to_sec(h1, m1, s1))

def main():
    hms_start = input()
    hms_end = input()
    h1, m1, s1 = str2hms(hms_start)
    h2, m2, s2 = str2hms(hms_end)
    h, m, s = diff(h1, m1, s1, h2, m2, s2)
    print(hms2str(h, m, s))

exec(input())