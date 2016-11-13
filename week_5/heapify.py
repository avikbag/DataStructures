import sys
import time
import random

result = []

def isEven(n):
	if (n % 2 == 0):
		return True
	else:
		return False

def parent(n):
	if isEven(n) == True:
		return ((n-1)/2)
	else:
		return (n/2)

def swap(i, j):
	global result
	temp = result[i]
	result[i] = result[j]
	result[j] = temp

def percolate_up(i):
	global result
	if i != 0: ## Checks if the list contains more than one element
		if result[i] < result[parent(i)]: ## Checks if the node is less than the parent node
			swap(i,parent(i))
			return percolate_up(parent(i))

def heapify(input_A):
	global result
	result = []
	i = 0
	for x in input_A:
		result.append(x)
		percolate_up(i)
		i += 1 

def main(argv):
	while True:
		try:
			test = (raw_input()).split()
		except (EOFError):
			break;
		test = [int(x) for x in test]
		global result
		heapify(test)
		for x in test:
			print "%i "%x,
		print 
		for x in result:
			print "%i "%x,
		print "\n"

if __name__ == "__main__":
	main(sys.argv)
		
