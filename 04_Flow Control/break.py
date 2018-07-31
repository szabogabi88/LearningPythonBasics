# prime numbers from 2..n-1

n = int(input("Enter an integer(n)"))

for i in range(2,n):
	if n % i == 0:
		print(n,'equals',i,'*',n//i)
		break
else:
	# this code runs, when no break occurs!!!
	# it belongs to for loop!
	print(n, 'is a prime number')
