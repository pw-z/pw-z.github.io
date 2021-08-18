#include "binary_tree_1.h"
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

int main(int argc, char const *argv[])
{
    Node a,b,c,d,e,f,g;
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
    in_order_traverse(&a);
    cout<<endl;
    post_order_traverse(&a);
    cout<<endl;


    return 0;
}
