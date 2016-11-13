import sys

def fibonacci(n):
	if n < 0:
		print "Invalid Index"
	elif n == 0:
		return 1
	elif n == 1:
		return 1
	else:
		return fibonacci(n-2)+fibonacci(n-1)

def main(argv):
	n = int(argv[0])
	result = fibonacci(n)
	print "The number is %i" %result

if __name__ == "__main__":
	main(sys.argv[1:])