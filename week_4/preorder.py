import math
import sys

parseTree = [] # global parse tree array

def evaluate(i): #argument takes index of 0 (start of the list)
	if i < len(parseTree):
		if parseTree[i] == '+':
			del parseTree[i]
			return evaluate(i) + evaluate(i)
		elif parseTree[i] == '-':
			del parseTree[i]
			return evaluate(i) - evaluate(i)
		elif parseTree[i] == '*':
			del parseTree[i]
			return evaluate(i) * evaluate(i)
		elif parseTree[i] == '/':
			del parseTree[i]
			return evaluate(i) / evaluate(i)
		else:
			element = parseTree[i]
			del parseTree[i]
			return int(element)

def pre2in(i): #argument takes index of 0 (start of the list)
	if i < len(parseTree):
		if parseTree[i] == '+':
			del parseTree[i]
			return " ( " + pre2in(i) + " + " + pre2in(i) + " ) "
		elif parseTree[i] == '-':
			del parseTree[i]
			return " ( " + pre2in(i) + " - " + pre2in(i) + " ) "
		elif parseTree[i] == '*':
			del parseTree[i]
			return " ( " + pre2in(i) + " * " + pre2in(i) + " ) "
		elif parseTree[i] == '/':
			del parseTree[i]
			return " ( " + pre2in(i) + " / " + pre2in(i) + " ) "
		else:
			element = parseTree[i]
			del parseTree[i]
			return element

def pre2post(i): #argument takes index of 0 (start of the list)
	if i < len(parseTree):
		if parseTree[i] == '+':
			del parseTree[i]
			return pre2post(i) + " " + pre2post(i) + " + "
		elif parseTree[i] == '-':
			del parseTree[i]
			return pre2post(i) + " " + pre2post(i) + " - "
		elif parseTree[i] == '*':
			del parseTree[i]
			return pre2post(i) + " " + pre2post(i) + " * "
		elif parseTree[i] == '/':
			del parseTree[i]
			return pre2post(i) + " " + pre2post(i) + " / "
		else:
			element = parseTree[i]
			del parseTree[i]
			return element

def main(argv):
	test = raw_input()
	while test:
		print "pre: " + test
		global parseTree
		parseTree = test.split()
		output = pre2in(0)
		output = output.replace("  ", ' ') ## To get rid of occurences of double spaces
		print "in: " + output

		parseTree = test.split()
		output = pre2post(0)
		output = output.replace("  ", ' ') ## To get rid of occurences of double spaces
		print "post: " + output

		parseTree = test.split()
		output = evaluate(0)
		print "eval: %i"%output

		try:
			test = raw_input()
		except(EOFError):
			break;

if __name__ == "__main__":
	main(sys.argv)