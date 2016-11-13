COMPILER=python
p1=./problem1.py
p2=./problem2.py

problem1: $(p1)
	$(COMPILER) $(p1)
problem2: $(p2)
	$(COMPILER) $(p2)

run: $(p1) $(p2)
	$(COMPILER) $(p1) < $(input)
	$(COMPILER) $(p2) < $(input)

