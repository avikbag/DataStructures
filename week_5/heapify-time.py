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
	i = 1
	while i <= 10:
		test = random.sample(range(1,200*i), 100*i)
		global result
		start = time.clock()
		heapify(test)
		stop = time.clock()
		print "%i\t"%(100*i),
		print (stop - start)*1000,
		print
		i += 1

if __name__ == "__main__":
	main(sys.argv)
		
