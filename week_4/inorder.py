import math
import sys

parseTree = [] # global parse tree array


def evaluate(): #argument takes index of 0 (start of the list)
	i = 0
	global parseTree
	parseTree = [item for item in parseTree if item != '(']
	while i < len(parseTree):
		if parseTree[i] == ')':
			if parseTree[i - 2] == '+':
				x = int(parseTree[i - 3]) + int(parseTree[i - 1])
				i = i - 3
				parseTree.pop(i)
				parseTree.pop(i)
				parseTree.pop(i)
				parseTree.pop(i)
				parseTree.insert(0, x)

			elif parseTree[i - 2] == '-':
				x = int(parseTree[i - 3]) - int(parseTree[i - 1])
				i = i - 3
				parseTree.pop(i)
				parseTree.pop(i)
				parseTree.pop(i)
				parseTree.pop(i)
				parseTree.insert(0, x)

			elif parseTree[i - 2] == '*':
				x = int(parseTree[i - 3]) * int(parseTree[i - 1])
				i = i - 3
				parseTree.pop(i)
				parseTree.pop(i)
				parseTree.pop(i)
				parseTree.pop(i)
				parseTree.insert(0, x)

			elif parseTree[i - 2] == '/':
				x = int(parseTree[i - 3]) / int(parseTree[i - 1])
				i = i - 3
				parseTree.pop(i)
				parseTree.pop(i)
				parseTree.pop(i)
				parseTree.pop(i)
				parseTree.insert(0, x)

		i += 1
	
	return parseTree[0]

def in2pre(): #argument takes index of 0 (start of the list)
	i = 0
	global parseTree
	parseTree = [item for item in parseTree if item != '(']
	while i < len(parseTree):
		if parseTree[i] == ')':
			if parseTree[i - 2] == '+':
				x = ' + ' + parseTree[i - 3] + " " + parseTree[i - 1]
				i = i - 3
				parseTree.pop(i)
				parseTree.pop(i)
				parseTree.pop(i)
				parseTree.pop(i)
				parseTree.insert(0, x)

			elif parseTree[i - 2] == '-':
				x = ' - ' + parseTree[i - 3] + " " + parseTree[i - 1]
				i = i - 3
				parseTree.pop(i)
				parseTree.pop(i)
				parseTree.pop(i)
				parseTree.pop(i)
				parseTree.insert(0, x)

			elif parseTree[i - 2] == '*':
				x = ' * ' + parseTree[i - 3] + " " + parseTree[i - 1]
				i = i - 3
				parseTree.pop(i)
				parseTree.pop(i)
				parseTree.pop(i)
				parseTree.pop(i)
				parseTree.insert(0, x)

			elif parseTree[i - 2] == '/':
				x = ' / ' + parseTree[i - 3] + " " + parseTree[i - 1]
				i = i - 3
				parseTree.pop(i)
				parseTree.pop(i)
				parseTree.pop(i)
				parseTree.pop(i)
				parseTree.insert(0, x)

		i += 1
	
	return parseTree[0]

def in2post(): #argument takes index of 0 (start of the list)
	i = 0
	global parseTree
	parseTree = [item for item in parseTree if item != '(']
	while i < len(parseTree):
		if parseTree[i] == ')':
			if parseTree[i - 2] == '+':
				x = parseTree[i - 3] + " " + parseTree[i - 1] + ' + '
				i = i - 3
				parseTree.pop(i)
				parseTree.pop(i)
				parseTree.pop(i)
				parseTree.pop(i)
				parseTree.insert(0, x)

			elif parseTree[i - 2] == '-':
				x = parseTree[i - 3] + " " + parseTree[i - 1] + ' - '
				i = i - 3
				parseTree.pop(i)
				parseTree.pop(i)
				parseTree.pop(i)
				parseTree.pop(i)
				parseTree.insert(0, x)

			elif parseTree[i - 2] == '*':
				x = parseTree[i - 3] + " " + parseTree[i - 1] + ' * '
				i = i - 3
				parseTree.pop(i)
				parseTree.pop(i)
				parseTree.pop(i)
				parseTree.pop(i)
				parseTree.insert(0, x)

			elif parseTree[i - 2] == '/':
				x = parseTree[i - 3] + " " + parseTree[i - 1] + ' / '
				i = i - 3
				parseTree.pop(i)
				parseTree.pop(i)
				parseTree.pop(i)
				parseTree.pop(i)
				parseTree.insert(0, x)

		i += 1
	
	return parseTree[0]

def main(argv):
	test = raw_input()
	while test:
		global parseTree
		parseTree = test.split()
		output = in2pre()
		output = output.replace("  ", ' ') ## To get rid of occurences of double spaces
		print "pre: " + output

		print "in: " + test

		parseTree = test.split()
		output = in2post()
		output = output.replace("  ", ' ') ## To get rid of occurences of double spaces
		print "post: " + output

		parseTree = test.split()
		output = evaluate()
		print "eval: %i"%output

		try:
			test = raw_input()
		except(EOFError):
			break;

if __name__ == "__main__":
	main(sys.argv)
