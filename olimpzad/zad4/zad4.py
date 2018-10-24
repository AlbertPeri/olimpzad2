with open('input.txt', 'r', encoding='utf-8') as f:
    n = f.readline()
    n = int(n)
    np, sh = list(), list()
    for _ in range(n):
        u = f.readline()
        p, h = u.split(" ")
        p, h = int(p), int(h)
        np.append(p)
        sh.append(h)

x, y = 0.0, 0.0
print(np, sh)
for i in range(n):
    if np[i] == 1 or np[i] == 2 or np[i] == 8:
        y += sh[i]
    if np[i] == 3 or np[i] == 2 or np[i] == 4:
        x += sh[i]
    if np[i] == 5 or np[i] == 6 or np[i] == 4:
        y -= sh[i]
    if np[i] == 7 or np[i] == 6 or np[i] == 8:
        x -= sh[i]

print(x, y)

with open('output.txt', 'w', encoding='utf-8') as f:
    f.write(str(x))
    f.write(" ")
    f.write(str(y))