def fib(n):    # write Fibonacci series up to n
	"""Print a Fibonacci series up to n.
	>>> [fib(10)]
	[[0, 1, 1, 2, 3, 5, 8]]

	"""
	a, b = 0, 1
	l = [0,1]
	i = 2
	while l[i-1] +l[i-2] < n:
		l.append(l[i-1] +l[i-2])
		i = i + 1
	return l

if __name__ == "__main__":
	import doctest
	doctest.testmod()