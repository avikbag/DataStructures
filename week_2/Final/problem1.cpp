#include <iostream>
#include <string>
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
	l1 = generateList(4);
	Node* l2;
	l2 = generateList(7);
	
	cout << "\n ---------------------- Problem1 ----------------------" << endl;

	Node* res;
	res = list_concat(l1, l2);
	cout << "Concatenated List using list_concat" << endl;
	printList(res);

	// Check 
	Node* t = l1->nextLink();
	t->setData(100);
	t = t->nextLink();
	t->setData(200);
	t = t->nextLink();
	t->setData(300);

	//printList(res);
	cout << "Concatenated List after updating value in list l1" << endl;
	printList(res);
	
	return 0;
}