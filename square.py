
def square(n, fn = lambda x: x**2):

	return[fn(i) for i in range(n)]


print(square(10))

