#ifndef _BI_TREE_H_
#define _BI_TREE_H_

#include <iostream>

class Node
{
public:
    int data;
    Node* lchild, * rchild;
};


void pre_order_traverse(Node *root){
    if(root != nullptr){  // c++::nullptr ~~ c::null/NULL
        std::cout<<root->data<<" ";
        pre_order_traverse(root->lchild);
        pre_order_traverse(root->rchild);
    }
}

void in_order_traverse(Node *root){
    if(root != nullptr){
        in_order_traverse(root->lchild);
        std::cout<<root->data<<" ";
        in_order_traverse(root->rchild);
    }
}

void post_order_traverse(Node *root){
    if(root != nullptr){
        post_order_traverse(root->lchild);
        post_order_traverse(root->rchild);
        std::cout<<root->data<<" ";
    }
}

void level_order_traverse(Node *root){
    
}


#endif