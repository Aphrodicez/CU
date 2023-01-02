months =  ["", "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
zodiacs = ["", "Capricorn", "Aquarius", "Pisces", "Aries", "Taurus", "Gemini", 
           "Cancer", "Leo", "Virgo", "Libra", "Scorpio", "Sagittarius"]

qs = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for i in range(1, len(qs)):
    qs[i] += qs[i - 1]

def is_leap_year(y):
    return ((y % 4 == 0 and y % 100 != 0) or y % 400 == 0)

def day_of_year(d, m, y):
    return d + qs[m - 1] + (m > 2) * is_leap_year(y)

def read_date():
    d, m, y = input().split()
    return [int(d), months.index(m), int(y)]

def zodiac(d, m):
    return zodiacs[(m - 1 + (d >= 22)) % 12 + 1]

def days_in_feb(y):
    return 28 + is_leap_year(y)

def days_in_month(m, y):
    return qs[m] - qs[m - 1] if m != 2 else days_in_feb(y)

def days_in_between(d1, m1, y1, d2, m2, y2):
    if y1 == y2:
        return day_of_year(d2, m2, y2) - day_of_year(d1, m1, y1)
    sum1 = (qs[12] + is_leap_year(y1)) - (day_of_year(d1, m1, y1))
    sum2 = day_of_year(d2, m2, y2) - 1
    mid = 365 * (y2 - y1 - 1) + ((((y2 - 1) // 4) - ((y2 - 1) // 100) + ((y2 - 1) // 400)) - ((y1 // 4) - (y1 // 100) + (y1 // 400)))
    return sum1 + mid + sum2

def main() :
    d1, m1, y1 = read_date()
    d2, m2, y2 = read_date()
    print(zodiac(d1, m1), zodiac(d2, m2))
    print(days_in_between(d1, m1, y1, d2, m2, y2))

exec(input().strip())