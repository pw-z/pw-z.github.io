#include "mystring.h"
#include <ctime>
#include <iostream>

void test_best_for_kmp(){
    char ss1[] = "0000000000";
    char ss2[] = "0000000001";
    mystring::MyString s1 = mystring::MyString(ss1);
    mystring::MyString s2 = mystring::MyString(ss2);
    s1.print();
    s2.print();
    for (int i = 0; i < 100000; i++)
    {
        s1.append(ss1);
    }
    s1.append(ss2);
    int i;
    clock_t start, end;

    start = clock();
    i = mystring::index_plain(s1, s2);
    end = clock();
    std::cout<<"index_plain find ss2 at " <<i<<", cost: " << end - start << " CLOCKS" << std::endl;

    
    start = clock();
    i = mystring::index_KMP(s1, s2);
    end = clock();
    std::cout<<"index_KMP find ss2 at " <<i<<", cost: " << end - start <<" CLOCKS" << std::endl;
}

void test_worst_for_kmp(){
    char ss1[] = "0000000000";
    char ss2[] = "1111111111";
    mystring::MyString s1 = mystring::MyString(ss1);
    mystring::MyString s2 = mystring::MyString(ss2);
    s1.print();
    s2.print();
    for (int i = 0; i < 100000; i++)
    {
        s1.append(ss1);
    }
    s1.append(ss2);
    int i;
    clock_t start, end;

    start = clock();
    i = mystring::index_plain(s1, s2);
    end = clock();
    std::cout<<"index_plain find ss2 at " <<i<<", cost: " << end - start << " CLOCKS" << std::endl;

    
    start = clock();
    i = mystring::index_KMP(s1, s2);
    end = clock();
    std::cout<<"index_KMP find ss2 at " <<i<<", cost: " << end - start <<" CLOCKS" << std::endl;
}

int main(int argc, char const *argv[])
{
    test_best_for_kmp();
    test_worst_for_kmp();
    return 0;
}
/*
0000000000
0000000001
index_plain find ss2 at 1000010, cost: 51 CLOCKS
next[] = -1012345678
index_KMP find ss2 at 1000010, cost: 13 CLOCKS

0000000000
1111111111
index_plain find ss2 at 1000010, cost: 7 CLOCKS
next[] = -1012345678
index_KMP find ss2 at 1000010, cost: 10 CLOCKS
*/
