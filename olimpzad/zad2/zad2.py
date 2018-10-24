with open('input.txt', 'r', encoding='utf-8') as f:
	s = f.read()

a, h = s.split(" ")
a = int(a)
h = int(h)

x1, y1 = 0, 0
x2, y2 = a // 2, h
x3, y3 = a // 2, 0

hs = 0
for x0 in range(a // 2):
	for y0 in range(h):
		t1 = (x1 - x0) * (y2 - y1) - (x2 - x1) * (y1 - y0)
		t2 = (x2 - x0) * (y3 - y2) - (x3 - x2) * (y2 - y0)
		t3 = (x3 - x0) * (y1 - y3) - (x1 - x3) * (y3 - y0)
		if t1 == 0 or t2 == 0 or t3 == 0:
			continue
		if t1*t2 > 0 and t1*t3>0:
			hs += 1

s = h - 1 + hs * 2

with open('output.txt', 'w', encoding='utf-8') as f:
	f.write(str(s))
