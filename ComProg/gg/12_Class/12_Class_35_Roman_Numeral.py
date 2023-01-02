class roman :
    def __init__(self, r):
        self.roman = r
    
    def __lt__(self, rhs):
        return int(self) < int(rhs)

    def __str__(self):
        keys = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        values = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        arabic = int(self)
        roman = ''
        i = 0
        while arabic > 0:
            while arabic >= keys[i]:
                roman += values[i]
                arabic -= keys[i]
            i += 1
        return roman 

    def __int__(self):
        d = {'CM' : 900, 'CD' : 400, 'M' : 1000, 'D' : 500, 'XC' : 90, 'XL' : 40, 'C' : 100, 'L' : 50, 'IX' : 9, 'IV' : 4, 'X' : 10, 'V' : 5, 'I' : 1}
        keys = ['CM', 'CD', 'M', 'D', 'XC', 'XL', 'C', 'L', 'IX', 'IV', 'X', 'V', 'I']
        roman = self.roman
        for key in keys:
            roman = roman.replace(key, str(d[key]) + ' ')
        return sum([int(e) for e in roman.split()])
    
    def __add__(self, rhs):
        return roman(str(int(self) + int(rhs)))

t, r1, r2 = input().split() 
a = roman(r1)
b = roman(r2) 
if t == '1' :
    print(a < b) 
elif t == '2' :
    print(int(a), int(b))
elif t == '3' :
    print(str(a), str(b))
elif t == '4' :
    print(int(a + b)) 
else : print(str(a + b))