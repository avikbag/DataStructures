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
