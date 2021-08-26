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


int main(int argc, char const *argv[])
{
  // traverse_test();
  create_tree_in_level_order();

  return 0;
}

