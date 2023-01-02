def distance1(x1, y1, x2, y2):
	return ((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1)) ** 0.5

def distance2(p1, p2):
	return distance1(p1[0], p1[1], p2[0], p2[1])

def distance3(c1, c2):
	d = distance2(c1[:2], c2[:2])
	minr, maxr = c1[2], c2[2]
	if minr > maxr:
		minr, maxr = maxr, minr
	a, b, c = minr, maxr, d
	if maxr > d:
		b, c = c, b
	return (d, a + b >= c)

def perimeter(points):
	return sum(distance2(points[i], points[(i + 1) % len(points)]) for i in range(len(points )))

exec(input().strip())