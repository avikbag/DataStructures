#!/usr/bin/env python
import copy

def max_digits(input_data):
	max = 0
	for x in input_data:
		length = len(str(x))
		if length > max :
			max = length
	return max;

def radix(input_data):
	func = copy.deepcopy(input_data)
	n = max_digits(input_data)
	i = -1
	while i >= -n:
		bins = [[], [], [], [], [], [], [], [], [], []]
		for num in func:
			try:
				digit = (str(num))[i]
			except IndexError:
				digit = '0'
			bins[int(digit)].append(num)

		buckets = []
		for x in bins:
			for y in x:
				buckets.append(y)
		func = buckets
		i -= 1

	return buckets

def printList(input_data):
	for x in input_data:
		print ("%i ")%x,
	print 

def main():
	while True:
		try:
			test = (raw_input()).split()
		except (EOFError):
			break;
		test = [int(x) for x in test]
		res = radix(test)
		printList(res)

if __name__ == '__main__':
	main()