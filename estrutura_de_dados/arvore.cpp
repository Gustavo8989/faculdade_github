#include <iostream> 
using namespace std;

int main(){
    return 0;
}

struct Node {
    int data;
    Node *left;
    Node * right;

    Node(int val) : data(val), left(nullptr), right(nullptr) {}
}

Node* root = new Node(10);
root->left = new Node(5);
root->right = new Node(15);

