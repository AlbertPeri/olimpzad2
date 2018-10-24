with open('input.txt', 'r', encoding='utf-8') as f:
	number = f.read()

number = int(number)

l = len(bin(number)) - 2
n = 2 ** (l - 1)

start_number = number
mx = number
while True:
	last_n = int(bin(number)[- 1])
	number = number // 2
	if (last_n == 1):
		number += n
	if number > mx:
		mx = number
	if (start_number == number):
		break



with open('output.txt', 'w', encoding='utf-8') as f:
	f.write(str(mx))