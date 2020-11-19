// Add nodes operations on Single Linked List
// Add Operations: 1. Add at the head, 2. Add a node at a given position 3. Add at the end
// Author: Pavan Kumar Paluri

#include <iostream>
#include <vector>
using namespace std;

class Node{
public:
	int data;
	Node* next;
};

// traverse the linkedlist
void traverse_linkedlist(Node* root)
{
	while(root!=NULL)
	{
		cout << root->data << "->";
		root = root->next;
	}
	cout<<"NULL.";
	cout << endl;
}

// add node at the front of the linked list
Node* add_node_front(Node* head, int data)
{
	Node* new_node = new Node();
	new_node->data = data;
	if(head==NULL)
	{
		// make the new node the head 
		head = new_node;
		head->next = NULL;
	}
	else{
		new_node->next = head;
		head = new_node;
	}
	return head;
}

// add node given the pos to be inserted at into the linked list
Node* add_node(Node* head, int data1, int pos)
{
  Node* new_node = new Node();
  new_node->data = data1;
  int counter =1;
  Node* current = head;
  while(current!=NULL)
  {
  	if(counter==pos)
  	{
  		Node*temp = current->next;
  		current->next = new_node;
  		new_node->next = temp;
  	}
  	current=current->next;
  	counter ++;
  }
  return head;
}

// add node at the rear end of the LinkedList
Node* add_node_back(Node*head, int data2)
{
	Node* new_node = new Node();
	new_node->data = data2;
	if(head==NULL)
	{
		head = new_node;
		new_node->next = NULL;
		return head;
	}

	Node* current = head;
	while(current->next!=NULL)
		current=current->next;
	// if here: current is the last node
	current->next = new_node;
	new_node->next = NULL;
	return head;
}
// To create a simple Linked List with 3 nodes 
int main()
{
	// create 3 disjoint nodes
	Node* head = NULL;
	Node* second = NULL;
	Node* third = NULL;

	head = new Node();
	second = new Node();
	third = new Node();

	head->data = 1;
	head->next = second;

	second->data = 2;
	second->next = third;
 
	third->data = 3;
	third->next = NULL;

	int data = 4;
	int data1 = 5;
	int data2 = 9;
	int pos = 3;
	// Add a node at the front of the LinkedList
	Node*root =add_node_front(head, data);
	Node*root2 = add_node_back(root, data2);
	Node*root1 = add_node(root2, data1, pos);

	traverse_linkedlist(root1);
	return 0;
}
