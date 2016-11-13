CC=g++
CFLAGS=-O0
TARGET1=./problem1
TARGET2=./problem2
TARGET3=./problem3
OUTPUT=./mydata.txt
READER=vim

$(TARGET): problem1.o 
	$(CC) $(CFLAGS) -o $(TARGET) problem1.o
problem1.o: problem1.cpp
	$(CC) $(CFLAGS) -c problem1.cpp

$(TARGET): problem2.o 
	$(CC) $(CFLAGS) -o $(TARGET) problem2.o
problem2.o: problem2.cpp
	$(CC) $(CFLAGS) -c problem2.cpp

$(TARGET): problem3.o 
	$(CC) $(CFLAGS) -o $(TARGET) problem3.o
problem3.o: problem3.cpp
	$(CC) $(CFLAGS) -c problem3.cpp


clean:
	rm -f *.o $(TARGET1) $(TARGET2) $(TARGET3) $(OUTPUT)
run: $(TARGET1) $(TARGET2) $(TARGET3) view
	$(TARGET1) 
	$(TARGET2) 
	$(TARGET3) > $(OUTPUT)
view: func.cpp
	$(READER) func.cpp
