#include "mystring.h"
#include <iostream>

int main(int argc, char const *argv[])
{
    mystring::MyString s1 = mystring::MyString();
    mystring::MyString s2 = mystring::MyString("test string 2");
    s1.print();
    s2.print();

    return 0;
}
