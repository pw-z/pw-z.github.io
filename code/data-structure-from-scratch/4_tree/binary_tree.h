#ifndef _BI_TREE_H_
#define _BI_TREE_H_

#include "queue.h"
#include "stack.h"
#include <iostream>

template <class Type>
class BiTNode
{
public:
    Type data;
    BiTNode<Type>* lchild;
    BiTNode<Type>* rchild;
};


template <class Type>
void pre_order_traverse(BiTNode<Type> *root){
    if(root != nullptr){  // c++::nullptr ~~ c::null/NULL
        std::cout<<root->data<<" ";
        pre_order_traverse(root->lchild);
        pre_order_traverse(root->rchild);
    }
}

template <class Type>
void in_order_traverse(BiTNode<Type> *root){
    if(root != nullptr){
        in_order_traverse(root->lchild);
        std::cout<<root->data<<" ";
        in_order_traverse(root->rchild);
    }
}

template <class Type>
void post_order_traverse(BiTNode<Type> *root){
    if(root != nullptr){
        post_order_traverse(root->lchild);
        post_order_traverse(root->rchild);
        std::cout<<root->data<<" ";
    }
}


template <class Type>
void pre_order_traverse_non_recursive(BiTNode<Type> *root){
    Stack<BiTNode<Type>*> stack;
    BiTNode<Type> *p = root;
    while (p || !stack.isempty())
    {
        if(p){
            std::cout<<p->data<<" ";
            stack.push(p);
            p = p->lchild;
        }else{
            p = stack.pop();
            p = p->rchild;
        }
    }
}

template <class Type>
void in_order_traverse_non_recursive(BiTNode<Type> *root){
    Stack<BiTNode<Type>*> stack;
    BiTNode<Type> *p = root;
    while (p || !stack.isempty())
    {
        if(p){
            stack.push(p);
            p = p->lchild;
        }else{
            p = stack.pop();
            std::cout<<p->data<<" ";
            p = p->rchild;
        }
    }
}
template <class Type>
void post_order_traverse_non_recursive(BiTNode<Type> *root){
    Stack<BiTNode<Type>*> stack;
    BiTNode<Type> *p = root;
    do{
        if(p->lchild != nullptr){
            stack.push(p->lchild);
            p = p->lchild;
        }else if (p->rchild != nullptr)
        {
            stack.push(p->rchild);
            p = p->rchild;
        }else{
            
        }
        
    }while (!stack.isempty())
}

template <class Type>
void level_order_traverse(BiTNode<Type> *root){
    Queue<BiTNode<Type>*> queue;
    BiTNode<Type>* p = root;
    queue.enqueue(p);
    while (!queue.isempty())
    {
        p = queue.dequeue();
        std::cout<<p->data<<" ";
        if(p->lchild)queue.enqueue(p->lchild);
        if(p->rchild)queue.enqueue(p->rchild);
    }
}


#endif