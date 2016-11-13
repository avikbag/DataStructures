import math
import sys

parseTree = [] # global parse tree array


def evaluate(): #argument takes index of 0 (start of the list)
	i = 0
	stack = [] # stack
	while i < len(parseTree):
		if parseTree[i] == '+':
			x = stack[-2] + stack[-1]
			stack.pop()
			stack.pop()
			stack.append(x)
			
		elif parseTree[i] == '-':
			x = stack[-2] - stack[-1]
			stack.pop()
			stack.pop()
			stack.append(x)
			
		elif parseTree[i] == '*':
			x = stack[-2] * stack[-1]
			stack.pop()
			stack.pop()
			stack.append(x)
			
		elif parseTree[i] == '/':
			x = stack[-2] / stack[-1]
			stack.pop()
			stack.pop()
			stack.append(x)

		else:
			stack.append(int(parseTree[i]))

		i += 1

	return stack[0]

def post2in(): #argument takes index of 0 (start of the list)
	i = 0
	stack = [] # stack
	while i < len(parseTree):
		if parseTree[i] == '+':
			x = " ( " + stack[-2] + " + " + stack[-1] + " ) "
			stack.pop()
			stack.pop()
			stack.append(x)
			
		elif parseTree[i] == '-':
			x = " ( " + stack[-2] + " - " + stack[-1] + " ) "
			stack.pop()
			stack.pop()
			stack.append(x)
			
		elif parseTree[i] == '*':
			x = " ( " + stack[-2] + " * " + stack[-1] + " ) "
			stack.pop()
			stack.pop()
			stack.append(x)
			
		elif parseTree[i] == '/':
			x = " ( " + stack[-2] + " / " + stack[-1] + " ) "
			stack.pop()
			stack.pop()
			stack.append(x)

		else:
			stack.append(parseTree[i])
		i += 1

	return stack[0]

def post2pre(): #argument takes index of 0 (start of the list)
	i = 0
	stack = [] # stack
	while i < len(parseTree):
		if parseTree[i] == '+':
			x = " + " + stack[-2] + " " +  stack[-1]
			stack.pop()
			stack.pop()
			stack.append(x)
			
		elif parseTree[i] == '-':
			x = " - " + stack[-2] + " " +  stack[-1]
			stack.pop()
			stack.pop()
			stack.append(x)
			
		elif parseTree[i] == '*':
			x = " * " + stack[-2] + " " +  stack[-1]
			stack.pop()
			stack.pop()
			stack.append(x)
			
		elif parseTree[i] == '/':
			x = " / " + stack[-2] + " " +  stack[-1]
			stack.pop()
			stack.pop()
			stack.append(x)

		else:
			stack.append(parseTree[i])

		i += 1
	
	return stack[0]

def main(argv):
	test = raw_input()
	while test:
		global parseTree
		parseTree = test.split()
		output = post2pre()
		output = output.replace("  ", ' ') ## To get rid of occurences of double spaces
		print "pre: " + output

		parseTree = test.split()
		output = post2in()
		output = output.replace("  ", ' ') ## To get rid of occurences of double spaces
		print "in: " + output

		print "post: " + test

		parseTree = test.split()
		output = evaluate()
		print "eval: %i"%output

		try:
			test = raw_input()
		except(EOFError):
			break;

if __name__ == "__main__":
	main(sys.argv)