#ifndef _BI_TREE_H_
#define _BI_TREE_H_

#include "queue.h"
#include "stack.h"
#include <iostream>
#include <string>

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

// !!!!
template <class Type>
void post_order_traverse_non_recursive(BiTNode<Type> *root){
    Stack<BiTNode<Type>*> stack;
    BiTNode<Type> *p = root, *last_visited;
    while(p || !stack.isempty())
    {
        if(p){  // visit left child utill meet leaf
            stack.push(p);
            p = p->lchild;
        }else{
            {
                // get top item of the stack
                // there is no top() method
                // using pop() + push() to emulate
                p = stack.pop();
                stack.push(p);
            }
            if(p->rchild && p->rchild!=last_visited){
                // visit right child tree
                p = p->rchild;
                // jump to visit left child utill meet leaf
            }else{
                // right child has been visited or is null
                // now visit the root of the current tree
                p = stack.pop();
                std::cout<<p->data<<" ";
                last_visited = p;
                p = nullptr;  // make p as a null left node
            }
        }
    }
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


// create_tree_in_level_order
BiTNode<int>* bitree_generator(std::string* seq, int length, int loc){
    if(loc <= length && seq[loc-1] != "#"){
        BiTNode<int>* root = new BiTNode<int>();
        root->data = atoi(seq[loc-1].c_str());
        // std::cout<<root->data<<"$$$$$$$$\n";
        root->lchild = bitree_generator(seq, length, loc*2);
        root->rchild = bitree_generator(seq, length, loc*2+1);
        return root;
    }else{
        return nullptr;
    }
}
BiTNode<int>* create_tree_in_level_order(){
    const int MAX_NODE_AMOUNT = 100;
    std::cout<<"input node in level order to create a binary tree.\n";
    std::cout<<"only integers and '#' allowed, max node amount = " << MAX_NODE_AMOUNT << "\n";
    std::cout<<"'#' means null node.\n";
    std::cout<<"for instance:\n";
    std::cout<<" ─a=1\n";
    std::cout<<"   ├─b=2\n";
    std::cout<<"   │  ├─d=null\n";
    std::cout<<"   │  └─e=5\n";
    std::cout<<"   └─c=3\n";
    std::cout<<"      ├─f=6\n";
    std::cout<<"      └─g=7\n";
    std::cout<<"you should input '1 2 3 # 5 6 7'\n";
    std::cout<<"please input node sequence in one line:\n";

    std::string input;
    std::getline(std::cin, input);
    input.append(" ");
    // std::cout<<input<<"\n";
    std::string nodes[MAX_NODE_AMOUNT];
    int cur = 0;
    int last_pos = 0;
    for (int i = 0; i < input.length(); i++)
    {
        if(input[i] == ' '){
            std::string temp = input.substr(last_pos, i-last_pos);
            // std::cout<<temp<<"\n";
            // node[cur++] = atoi(temp.c_str());
            nodes[cur++] = temp;
            // std::cout<<node[cur -1]<<"\n";
            last_pos = i+1;
        }
    }
    // for (int i = 0; i < cur; i++){std::cout<<node[i]<<" ";}
    
    BiTNode<int>* the_tree = bitree_generator(nodes, cur, 1);
    // every node in this tree is created by 'new' operator
    // GC operation is necessary
    return the_tree;
}


// tree printer
template <class Type>
void pre_order_traverse_for_tree_printer(BiTNode<Type> *root, std::string padding, std::string turning, bool has_right_sibling){
    if(root != nullptr){  // c++::nullptr ~~ c::null/NULL
        std::cout<<padding;
        std::cout<<turning;
        std::cout<<root->data<<"\n";

        /****************recursive***************/
        if (has_right_sibling){
            padding += "│  ";
        }else{
            padding += "   ";
        }
        std::string to_left = (root->rchild != nullptr) ? "├──" : "└──";
        pre_order_traverse_for_tree_printer(root->lchild, padding, to_left, root->rchild != nullptr);
        pre_order_traverse_for_tree_printer(root->rchild, padding, "└──", false);
        /****************recursive***************/


        /****************note********************/
        // what if removing the `has_right_sibling` parameter and
        // replace the `recursive` block with the code below in `note_code`?
        // 
        // `padding` in current recursive layer needs to append a "|  " or "   ",
        // which one depends on whether its parents layer has the right sibling, 
        // that can be known at its parents' parents node, so this info needs to 
        // be sent in grandparents layers as we don't store parents info in the 
        // BiTNode, code in `note_code` will go wrong because `padding` is shared
        // in current layer and will be changed twice and what's more importent,
        // it's just pass the parents info to its children, not its grandchildren.
        /****************note********************/

        /****************note_code***************/
        // std::string to_left = (root->rchild != nullptr) ? "├──" : "└──";
        // pre_order_traverse_for_tree_printer(root->lchild, (root->rchild != nullptr ? padding+="│  ":"   "), to_left);
        // pre_order_traverse_for_tree_printer(root->rchild, padding+="   ", "└──");
        /****************note_code***************/
    }
}
template<class Type>
void tree_horizontal_printer(BiTNode<Type>* root){
    // this printer can't 
    std::cout<<root->data<<"\n";
    std::string to_left = (root->rchild != nullptr) ? "├──" : "└──";
    pre_order_traverse_for_tree_printer(root->lchild, "", to_left, root->rchild != nullptr);
    pre_order_traverse_for_tree_printer(root->rchild, "", "└──", false);
}


#endif