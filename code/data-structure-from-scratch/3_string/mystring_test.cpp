#include "mystring.h"
#include <iostream>


void test1(){
    char s[] = "test string 1";
    mystring::MyString s1 = mystring::MyString();
    mystring::MyString s2 = mystring::MyString(s);
    s1.print();
    s2.print();
    s2.clear();
    s2.print();
    std::cout<<s1.isempty()<<std::endl;
    std::cout<<s2.isempty()<<std::endl;
    s1.append(s);
    s1.append(s);
    s1.print();
    std::cout<<s1.length()<<std::endl;
    s1.remove(0,3);
    s1.print();
    std::cout<<s1.length()<<std::endl;
    s1.clear();
    std::cout<<s1.length()<<std::endl;
}
/*

test string 1

1
1
test string 1test string 1
26
 string 1test string 1
22
0
*/

void test2(){
    char ss1[] = "test string 1";
    char ss2[] = "test string 2";
    mystring::MyString s1 = mystring::MyString(ss1);
    mystring::MyString s2 = mystring::MyString(ss2);
    s1.print();
    s2.print();
    // bool result = mystring::compare(s1, s2);
    // std::cout<< result << std::endl;
    char* s3 = mystring::substring(s2, 0, 1);
    std::cout<< s3<<"\n";
}

void test3(){
    char ss[] = "jfkdlskdjflsadf";
    mystring::MyString s1 = mystring::MyString();
    mystring::MyString s2 = mystring::MyString(ss);
    s1.print();
    s2.print();
    s1 = s2;
    s1.print();
}

int main(int argc, char const *argv[])
{
    // test1();
    // test2();
    test3();
    return 0;
}
