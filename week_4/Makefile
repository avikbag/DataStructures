COMPILER=python
prog1=preorder.py
prog2=inorder.py
prog3=postorder.py

pre: $(prog1)
	$(COMPILER) $(prog1)

in: $(prog2)
	$(COMPILER) $(prog2)

post: $(prog3)
	$(COMPILER) $(prog3)

run: $(prog1) $(prog2) $(prog3)
	$(COMPILER) $(prog1) < $(pre)
	$(COMPILER) $(prog2) < $(in)
	$(COMPILER) $(prog3) < $(post)