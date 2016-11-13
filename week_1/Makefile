CC=g++
CFLAGS=-O0
TARGET=./hello
READER=vim

$(TARGET): hello.o
	$(CC) $(CFLAGS) -o $(TARGET) hello.o
hello.o: hello.cpp
	$(CC) $(CFLAGS) -c hello.cpp
clean:
	rm -f *.o $(TARGET)
run: $(TARGET)
	$(TARGET)
view: hello.cpp
	$(READER) hello.cpp
