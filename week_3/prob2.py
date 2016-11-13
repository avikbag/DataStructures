import sys

memo = [1]*100;

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

def main(argv):
	n = int(argv[0])
	result = fibonacci_memo(n)
	print "The number is %i" %result

if __name__ == "__main__":
	main(sys.argv[1:])