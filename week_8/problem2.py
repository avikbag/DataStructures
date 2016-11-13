import sys
import copy

INF = 9999999
def extract():
	input_data = []
	line = raw_input()
	while(line):
		input_data.append(line.split())
		try:
			line = raw_input()
		except(EOFError):
			break;
	return input_data

def initialize(raw_data):
	result = []
	for x in range(0,len(raw_data)):
		init = [INF] * (len(raw_data))
		result.append(init)
	for i in range(0,len(raw_data)):
		result[i][i] = 0
	return result

def costMatrix(input_data):
	matrix = initialize(input_data)
	for x in input_data:
		if len(x) > 1:
			i = int(x[0])
			for y in range(1,len(x)):
				j = int((x[y].split(','))[0])
				cost = int((x[y].split(','))[1])
				matrix[i][j] = cost
				matrix[j][i] = cost
	return matrix

def floyds(cost):
	res = copy.deepcopy(cost)
	n = len(res)
	for k in range(0, n):
		for i in range(0, n):
			for j in range(0, n):
				if res[i][k] + res[k][j] < res[i][j]:
					res[i][j] = res[i][k] + res[k][j]
					# res[j][i] = res[i][k] + res[k][j]
	return res

def floyds_path(cost):
	p = []
	n = len(cost)
	printMatrix(cost)
	res = copy.deepcopy(cost)
	for x in range(0,n):
		init = [0] * n
		p.append(init)
	for x in range(0,n):
		for y in range(0,n):
			if x==y:
				p[x][y] = x
			elif (cost[x][y] != INF):
				p[x][y] = y
				p[y][x] = x
			else:
				p[x][y] = -1
				p[y][x] = -1
	printMatrix(p)
	for k in range(0, n):
		for i in range(0, n):
			for j in range(0, n):
				if res[i][k] + res[k][j] < res[i][j]:
					res[i][j] = res[i][k] + res[k][j]
					p[i][j] = p[i][k]
	return p

def printMatrix(matrix):
	n = len(matrix)
	s = " "
	inf = "in"
	print ("%2s")%s,
	for i in range(0,n):
		print ("%2i")%i,
	print ("")
	for j in range(0,n):
		print ("%2i")%j,
		for k in range(0,n):
			if matrix[j][k] == INF:
				print ("%2s")%inf,
			else:
				print ("%2i")%matrix[j][k],
		print("")
			
def path(p,i,j):
	k = p[i][j]
	if k == 0:
		return 0 
	path(p,i,k)
	print k
	path(p,k,j)

def main(argv):
	raw_data = extract()
	C = costMatrix(raw_data)
	# fin = floyds(C)
	# printMatrix(C)
	# printMatrix(fin)
	p = floyds_path(C)
	printMatrix(p)
	
if __name__ == "__main__":
	main(sys.argv)

