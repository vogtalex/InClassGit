def findDivisors(num , arr):
	x = 1
	i = 0
	while x <= num:
		if (num % x == 0):
			arr.append(x)
			i = i + 1
		x = x + 1

print('\nWelcome to the divisior program')

num = int(input("Enter a number to find the divisors of: "))
arr = []

findDivisors(num, arr)

x = len(arr)
i = 0

while i < x:
	print(arr[i])
	i = i + 1