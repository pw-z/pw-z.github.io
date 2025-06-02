# Data Structure from Scratch: Binary Tree

*Posted on 2021.08.31 by [pwz](http://pwz.wiki) under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)* 


- [1. Binary Tree Node Class](#1-binary-tree-node-class)
- [2. Binary Tree Traversal](#2-binary-tree-traversal)
  - [2.1. Recursive Traversal Algorithm](#21-recursive-traversal-algorithm)
    - [2.1.1. Preorder](#211-preorder)
    - [2.1.2. Inorder](#212-inorder)
    - [2.1.3. Postorder](#213-postorder)
  - [2.2. Non-Recursive Traversal Algorithm](#22-non-recursive-traversal-algorithm)
    - [2.2.1. Preorder](#221-preorder)
    - [2.2.2. Inorder](#222-inorder)
    - [2.2.3. Postorder](#223-postorder)
    - [2.2.4. Level Order](#224-level-order)
  - [2.3. Test](#23-test)
- [3. Create a Binary Tree in Level Order](#3-create-a-binary-tree-in-level-order)
  - [3.1. Implementation](#31-implementation)
  - [3.2. Test](#32-test)
- [4. Horizontal Tree Printer](#4-horizontal-tree-printer)
  - [4.1. Implementation](#41-implementation)
  - [4.2. Test](#42-test)
- [5. Reference & Readmore](#5-reference--readmore)


The `queue.h` and the `stack.h` in [the previous post](../07/2021072901-data-structure-from-scratch-stack-and-queue.md) of this blog will be used below.

## 1. Binary Tree Node Class

Binary tree will be store in `binary linked list` in this post.

```c++
template <class Type>
class BiTNode
{
public:
    Type data;
    BiTNode<Type>* lchild;
    BiTNode<Type>* rchild;
};
```

## 2. Binary Tree Traversal

###  2.1. Recursive Traversal Algorithm

#### 2.1.1. Preorder

```c++
template <class Type>
void pre_order_traverse(BiTNode<Type> *root){
    if(root != nullptr){  // c++::nullptr ~~ c::null/NULL
        std::cout<<root->data<<" ";
        pre_order_traverse(root->lchild);
        pre_order_traverse(root->rchild);
    }
}
```

#### 2.1.2. Inorder

```c++
template <class Type>
void in_order_traverse(BiTNode<Type> *root){
    if(root != nullptr){
        in_order_traverse(root->lchild);
        std::cout<<root->data<<" ";
        in_order_traverse(root->rchild);
    }
}
```

#### 2.1.3. Postorder

```c++
template <class Type>
void post_order_traverse(BiTNode<Type> *root){
    if(root != nullptr){
        post_order_traverse(root->lchild);
        post_order_traverse(root->rchild);
        std::cout<<root->data<<" ";
    }
}
```


### 2.2. Non-Recursive Traversal Algorithm

#### 2.2.1. Preorder

```c++
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
```

#### 2.2.2. Inorder

```c++
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
```

#### 2.2.3. Postorder

```c++
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
```

#### 2.2.4. Level Order

```c++
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
```

### 2.3. Test

```c++
/***
  ─a=1
    ├─b=2
    │  ├─d=4
    │  └─e=5
    └─c=3
       ├─f=6
       └─g=7
 */

int traverse_test()
{
    BiTNode<int> a,b,c,d,e,f,g;
    a.data = 1;
    b.data = 2;
    c.data = 3;
    d.data = 4;
    e.data = 5;
    f.data = 6;
    g.data = 7;

    a.lchild = &b;
    a.rchild = &c;
    b.lchild = &d;
    b.rchild = &e;
    c.lchild = &f;
    c.rchild = &g;
    d.lchild = NULL;
    d.rchild = NULL;
    e.lchild = NULL;
    e.rchild = NULL;
    f.lchild = NULL;
    f.rchild = NULL;
    g.lchild = NULL;
    g.rchild = NULL;

    pre_order_traverse(&a);
    cout<<endl;
    pre_order_traverse_non_recursive(&a);
    cout<<endl;
    in_order_traverse(&a);
    cout<<endl;
    in_order_traverse_non_recursive(&a);
    cout<<endl;
    post_order_traverse(&a);
    cout<<endl;
    post_order_traverse_non_recursive(&a);
    cout<<endl;

    level_order_traverse(&a);
    cout<<endl;

    return 0;
}
/*
1 2 4 5 3 6 7 
1 2 4 5 3 6 7
4 2 5 1 6 3 7
4 2 5 1 6 3 7
4 5 2 6 7 3 1
4 5 2 6 7 3 1
1 2 3 4 5 6 7
*/
```

## 3. Create a Binary Tree in Level Order

### 3.1. Implementation

```c++
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
```

### 3.2. Test

```c++
int level_order_creation_test()
{
  // traverse_test();
  BiTNode<int>* root = create_tree_in_level_order();
  pre_order_traverse(root);
  cout<<endl;
  in_order_traverse(root);
  cout<<endl;
  post_order_traverse(root);
  cout<<endl;
  level_order_traverse(root);
  cout<<endl;

  return 0;
}
/*
input node in level order to create a binary tree.
only integers and '#' allowed, max node amount = 100
'#' means null node.
for instance:
 ─a=1
   ├─b=2
   │  ├─d=null
   │  └─e=5
   └─c=3
      ├─f=6
      └─g=7
you should input '1 2 3 # 5 6 7'
please input node sequence in one line:
1 2 3 4 5 6 7
1$$$$$$$$
2$$$$$$$$
4$$$$$$$$
5$$$$$$$$
3$$$$$$$$
6$$$$$$$$
7$$$$$$$$
1 2 4 5 3 6 7 
4 2 5 1 6 3 7
4 5 2 6 7 3 1
1 2 3 4 5 6 7 
*/
```


## 4. Horizontal Tree Printer

### 4.1. Implementation

```c++
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
```

### 4.2. Test

```c++
void tree_printer_test(){
    BiTNode<int>* root = create_tree_in_level_order();
    tree_horizontal_printer(root);
}
/*
input node in level order to create a binary tree.
only integers and '#' allowed, max node amount = 100
'#' means null node.
for instance:
 ─a=1
   ├─b=2
   │  ├─d=null
   │  └─e=5
   └─c=3
      ├─f=6
      └─g=7
you should input '1 2 3 # 5 6 7'
please input node sequence in one line:
0 1 2 3 4 5 6 7 # # # # # # # 8 9
0
├──1
│  ├──3      
│  │  └──7   
│  │     ├──8
│  │     └──9
│  └──4      
└──2
   ├──5      
   └──6 
*/
```

## 5. Reference & Readmore

* [How to Print a Binary Tree Diagram](https://www.baeldung.com/java-print-binary-tree-diagram)
* [如何直观形象地树状打印一棵二叉树？](https://www.cnblogs.com/mjios/p/10627814.html)
* [二叉树控制台可视化](https://hotsnow-sean.github.io/posts/binarytree-condole-visualization/)
* [由二叉树的层序遍历构建二叉树(2种方法实现)](https://blog.csdn.net/weixin_37477009/article/details/109379809?utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7EBlogCommendFromMachineLearnPai2%7Edefault-1.essearch_pc_relevant&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7EBlogCommendFromMachineLearnPai2%7Edefault-1.essearch_pc_relevant)