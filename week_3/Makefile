COMPILER=python
P1=./prob1.py
P2=./prob2.py
P3=./prob3.py
OUTPUT=./mydata.txt

problem1: $(p1)
	$(COMPILER) $(P1) $(arg)

problem2: $(p2)
	$(COMPILER) $(P2) $(arg)

problem3: $(p3)
	$(COMPILER) $(P3) >$(OUTPUT)

clean:
	rm -Rf $(OUTPUT)
