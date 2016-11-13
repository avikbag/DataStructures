import sys
import copy

def Initialize(ar):
	temp = []
	my_set = []

	for x in ar:
		temp.append(x)
		my_set.append(list(temp))
		del temp[:]

	return my_set

def Find(my_set, val):
	for x in my_set:
		if val in x:
			return x
	return []

def Merge(my_set, a, b):
	set1 = copy.deepcopy(Find(my_set, a))
	set2 = copy.deepcopy(Find(my_set, b))

	if set1 != set2:
		if len(set1) > len(set2):
			rem = my_set.index(set2)
			rep = my_set.index(set1)
		else:
			rem = my_set.index(set1)
			rep = my_set.index(set2)

		if set1[-1] < set2[0]:
			set1 = set1 + set2
		else:
			set1 = set2 + set1

		my_set[rep] = set1
		my_set.pop(rem)

	# else:
		# print "values are already in the same set"
	
def main(argv):
	test = [1,2,3,4,5,6,7,8]
	myset = Initialize(test)
	print myset
	res = Find(myset, 6)
	print res
	Merge(myset, 2, 4)
	print myset
	Merge(myset, 5, 7)
	print myset
	Merge(myset, 6, 7)
	print myset
	Merge(myset, 5, 4)
	print myset
	Merge(myset, 5, 4)
	print myset
	res = Find(myset, 6)
	print res

if __name__ == "__main__":
	main(sys.argv)
	
