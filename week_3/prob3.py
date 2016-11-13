import time
import sys

memo = [1]*100;

def fibonacci(n):
	if n < 0:
		print "Invalid Index"
	elif n == 0:
		return 1
	elif n == 1:
		return 1
	else:
		return fibonacci(n-2)+fibonacci(n-1)

def fibonacci_memo(n):
	if n < 0:
		print "Invalid Index"
	elif n == 0:
		return memo[0]
	elif n == 1:
		return memo[1]
	else:
		if memo[n] != 1:
			return memo[n]
		else:
			memo[n] = fibonacci_memo(n-2)+fibonacci_memo(n-1)
			return memo[n]

def main():
	for x in range(1,41):
		# Timing for the recursive non-memoised function
		print ("%i\t"%x),
		start = time.clock()
		fibonacci(x)
		res = (time.clock() - start)*1000
		print ("%10.3f \t" %res),
		# Timing for the recursive memoised function
		start = time.clock()
		fibonacci_memo(x)
		res = (time.clock() - start)*1000
		print ("%10.3f \t\t" %res)

if __name__ == "__main__":
	main()
