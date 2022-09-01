from math import gcd

a, b, c = input().split(',')

value = [0, 0, 0]
coefficient = [0, 0, 0] 

value[0] = int(a)
try:
	value[1] = int(b)
except:
	pass
value[2] = int(c)

coefficient[1] = len(b)
coefficient[2] = len(c)
 
top = (value[0] * (10 ** coefficient[1]) + value[1]) * (10 ** coefficient[2]) + value[2]

top -= (value[0] * (10 ** coefficient[1]) + value[1])

bot = (10 ** (coefficient[1] + coefficient [2])) - (10 ** coefficient[1])

print(top // gcd(top, bot), bot // gcd(top, bot), sep = ' / ')