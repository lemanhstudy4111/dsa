#include <iostream>
using namespace std;

class Node
{
public:
    int value;
    Node *next;
    Node(int value, Node *next)
    {
        this->value = value;
        this->next = next;
    }
};

class LinkedList
{
public:
    Node *head;
    Node *tail;
    LinkedList(Node *head)
    {
        this->head = head;
        this->tail = head;
    };
    Node *prepend(int value)
    {
        Node *nextPtr = this->head;
        Node *newNode = new Node(value, nextPtr);
        this->head = newNode;
        return this->head;
    };
    Node *append(int value)
    {
        Node *newNode = new Node(value, nullptr);
        tail->next = newNode;
        this->tail = newNode;
        return this->tail;
    }
    int removeNode(int value)
    {
        Node *curr = head;
        if (curr->value == value)
        {
            this->head = this->head->next;
            return 1;
        }
        while (curr->next != nullptr)
        {
            if (curr->next->value == value)
            {
                Node *nextNode = curr->next;
                curr->next = curr->next->next;
                delete nextNode;
                nextNode = nullptr;
                return 1;
            }
        }
        return 0;
    }
    void printLinkedList()
    {
        Node *curr = head;
        while (curr != nullptr)
        {
            curr = curr->next;
            cout << "Node " << curr << ", data " << curr->value << endl;
        }
        return;
    }
};

int main()
{
    Node *head = new Node(1, nullptr);
    LinkedList *list = new LinkedList(head);
    for (int i = 2; i < 7; i++)
    {
        list->append(i);
    }
    list->printLinkedList();
    cout << "Done running" << endl;
    return 0;
}