// Deletion of nodes at various positions in a Single linked list
// Author: Pavan Kumar Paluri

#include <iostream>
#include <string>
#include <vector>

using namespace std;

class Node{
public:
	int data;
	Node* next;
};

// traverse the LinkedList
void print_LL(Node* root)
{
	// if root is Null
	if(root==NULL)
		cout<<"List is Empty"<<endl;
	else
	{
		while(root!=NULL)
		{
			cout<<root->data<<"->";
			root=root->next;
		}
		cout<<"None"<<endl;
	}

}

// delete a node at the beginning 
Node* delete_node_front(Node* root)
{
	if(root==NULL || root->next==NULL)
		// no node to delete / next one is nULL, so current one can be deleted
		return NULL;
	return root->next;
}

// Delete a node at a given position
Node* delete_node_mid(Node* root1, int pos)
{
	Node* root = root1;
	Node* temp = NULL;
	int counter =0;
	while(counter < pos)
	{
		temp = root;
		root=root->next;
		counter++;
	}
	// if here counter == pos
	Node* temp1 = root->next;
	root->next = NULL;
	temp->next= temp1;
	return root1;
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

int main()
{
	Node* head = NULL;
	Node* second = NULL;
	Node* third = NULL;

	head = new Node();
	second = new Node();
	third = new Node();

	head->data =1;
	second->data=2;
	third->data = 3;

	head->next = second;
	second->next = third;
	third->next = NULL;

	print_LL(head);
	Node* head2 = add_node_back(head, 4);
	print_LL(head2);
	Node* head3 = delete_node_mid(head2, 3);
	print_LL(head3);
	return 0;
}