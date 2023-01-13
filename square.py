def square(n, power=2):
'''(number variable, power variable) call for n to power; now with default of 2'''
	return[i**power for i in range(n)]

print(square(10))

