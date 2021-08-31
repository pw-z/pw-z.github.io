#include "binary_tree.h"
#include <iostream>

using namespace std;

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

int main(int argc, char const *argv[])
{
    // level_order_creation_test();
    tree_printer_test();
    return 0;
}
