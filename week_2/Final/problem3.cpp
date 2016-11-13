#include <iostream>
#include <string>
#include <ctime>
#include <cstdlib>
#include <iomanip>
using namespace std;

class Node
{
	public:
		// Constructor
		Node();
		Node(int d, Node *l = NULL);

		// Inspector
		int getData();
		Node* nextLink();

		// Mutator
		void setData(int d);
		void setLink(Node* l);

		// Destructor
		~Node();

	private:
		int data_;
		Node* link_;
};

//Implementation

Node::Node()
{
	link_ = NULL;
	data_ = 0;
}
Node::Node(int d, Node *l)
{
	link_ = l;
	data_ = d;
}
int Node::getData() 
{
	return data_;
}
Node* Node::nextLink() 
{
	return link_;
}
void Node::setData(int d)
{
	data_ = d;
}
void Node::setLink(Node* l)
{
	link_ = l;
}
Node::~Node()
{
	// avoid memory leaks by deleting the rest of the list
	if (link_ != NULL)
		delete link_;
}

// Functions based on linked lists
Node* generateList(int n) // Generates list of numbers from 1 to n
{
	Node* head = new Node();
	head->setData(1);
	
	Node* temp = new Node();
	temp->setData(2);

	head->setLink(temp);

	for(int i = 3; i<= n; i++)
	{
		temp->setLink(new Node(i));
		temp = temp->nextLink();
	}

	return head;
}

void printList(Node* head)
{
	if (head == NULL)
		cout << endl;
	else
	{
		cout << " -> " << head->getData() ;
		printList(head->nextLink());
	}
}

Node* list_concat(Node* A, Node* B)
{
	Node* res = new Node();
	res = A;
	Node* temp;
	temp = res->nextLink();
	Node* temp2;
	temp2 = res;
	while(temp != NULL)
	{
		temp = temp->nextLink();
		temp2 = temp2->nextLink();
	}
	temp2->setLink(B);
	
	return res;
}

Node* list_concat_copy(Node* A, Node* B)
{
	Node* res = new Node();
	Node* temp = new Node();
	Node* last = new Node();
	
	res = new Node(A->getData());
	temp = A->nextLink();
	Node* n = new Node(temp->getData());
	res->setLink(n);
	last = res;

	while(temp != NULL)
	{
		last->setLink(new Node(temp->getData()));
		last = last->nextLink();

		temp = temp->nextLink();
	}
	temp = B;
	while(temp != NULL)
	{
		last->setLink(new Node(temp->getData()));
		last = last->nextLink();

		temp = temp->nextLink();
	}
	return res;
}

// Main function
int main()
{
	Node* l1;
	Node* l2;
	Node* res;
	Node* res2;
	clock_t start, stop;
	int n = 1000;
	while (n <= 15000)
	{
		l1 = generateList(n);	
		l2 = generateList(n);
		
		cout << n << "\t";

		start = clock();
		res = list_concat_copy(l1, l2);
		stop = clock();
		cout << setw(8) << setfill('0') << left << fixed;
		cout << (((float)stop-(float)start)/(float)CLOCKS_PER_SEC) << "\t";


		start = clock();
		res2 = list_concat(l1, l2);
		stop = clock();
		cout << setw(8) << setfill('0') << left << fixed;
		cout << (((float)stop-(float)start)/(float)CLOCKS_PER_SEC) << "\t";
		
		n += 1000;
		cout << endl;
	}

	
	return 0;
}