A = int(input())
N = 0
for i in range(0,A):
	N+=1
	if (N**N)%A == 0:
		print(N)
		break