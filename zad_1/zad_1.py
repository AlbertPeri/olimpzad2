with open('input.txt', 'r', encoding='utf-8') as f:
	A = f.read()
A = int(A)
N = 0
for i in range(0,A):
	N+=1
	if (N**N)%A == 0:
		print(N)
		break
with open('output.txt', 'w', encoding='utf-8') as f:
	f.write(str(A))