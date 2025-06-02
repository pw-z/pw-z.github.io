# Data Structure from Scratch: String

*Posted on 2021.08.01 by [pwz](http://pwz.wiki) under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)* 

- [Data Structure from Scratch: String](#data-structure-from-scratch-string)
  - [1. MyString Implementation](#1-mystring-implementation)
    - [1.1. Class Implementation](#11-class-implementation)
    - [1.2. Non-class Methods](#12-non-class-methods)
  - [2. MyString Test](#2-mystring-test)
  - [3. Index Algorithms](#3-index-algorithms)
    - [3.1. Plain Algorithm](#31-plain-algorithm)
    - [3.2. KMP Algorithm](#32-kmp-algorithm)
    - [3.3. Performance Test](#33-performance-test)

## 1. MyString Implementation

### 1.1. Class Implementation
```c++
//mystring.h
#ifndef MYSTRING_H_
#define MYSTRING_H_

#include<iostream>

namespace mystring {

int mystrlen(char* s){
    int count = 0;
    while (s[count] != '\0')
    {
        count++;
    }
    return count;
}

static const int INIT_SIZE = 256;
static const int EXPAND_SIZE = 256;

class MyString
{
private:
    char* mystring_;
    int length_;
    int capacity_;
    bool expand(){
        char* temp = new char[capacity_ + EXPAND_SIZE];
        for (int i = 0; i < capacity_; i++)
        {
            temp[i] = mystring_[i];
        }
        delete [] mystring_;
        mystring_ = temp;
        capacity_ += EXPAND_SIZE;
        std::cout<<"expanded from "<<capacity_-EXPAND_SIZE<<" to "<<capacity_<<".\n";
        return true;
    }
public:
    MyString();
    MyString(char*);
    ~MyString();
    int length();
    bool isempty();
    bool append(char* s);
    bool remove(int start, int end);
    char get(int i);
    bool clear();
    void print();
};

MyString::MyString()
{
    mystring_ = new char [INIT_SIZE];
    length_ = 0;
    capacity_ = INIT_SIZE;
}

MyString::MyString(char* s){
    mystring_ = new char[INIT_SIZE];
    length_ = 0;
    capacity_ = INIT_SIZE;
    this->append(s);
}

MyString::~MyString()
{
    delete [] mystring_;
}

bool MyString::append(char* s){
    int string_size = mystring::mystrlen(s);
    while(length_ + string_size > capacity_){
        expand();
    }
    for (int i = 0; i < string_size; i++)
    {
        mystring_[length_ + i] = s[i];
    }
    length_ += string_size;
    mystring_[length_] = '\0';
    return true;
}

bool MyString::remove(int start, int end){
    if(start > end){
        std::cout<<"illegal index, start should smaller then end\n";
        return false;
    }
    if(start < 0 || end > length_){
        std::cout<<"illegal index, make sure that start>0 && end<str.length\n";
        return false;
    }
    for (int i = 0; i < length_-end-1; i++)
    {
        mystring_[start+i] = mystring_[end+i+1];
    }
    length_ -= end-start+1;
    mystring_[length_] = '\0';
    return true;
}

char MyString::get(int i){
    return mystring_[i];
}

bool MyString::isempty(){
    if(length_ == 0)
        return true;
    else
        return false;
}

int MyString::length(){
    return length_;
}

bool MyString::clear(){
    delete [] mystring_;
    mystring_ = new char[capacity_];
    length_ = 0;
    return true;
}

void MyString::print(){
    for (int i = 0; i < length_; i++)
    {
        std::cout<<mystring_[i];
    }
    std::cout<<"\n";
}

}//namespace mystring

#endif
```

### 1.2. Non-class Methods
```c++
//mysthing.h
bool compare(MyString &s1, MyString &s2){
    if(s1.length() != s2.length()){
        return false;
    }
    for (int i = 0; i < s1.length(); i++)
    {
        if(s1.get(i) != s2.get(i)){
            return false;
        }
    }
    return true;
}

char* substring(MyString &s, int start, int end){
    if(start > end){
        std::cout<<"illegal index, start should smaller then end\n";
        return NULL;
    }
    if(start < 0 || end > s.length()){
        std::cout<<"illegal index, make sure that start>0 && end<str.length\n";
        return NULL;
    }
    int size = end - start + 1;
    char* temp = new char[size];
    for (int i = 0; i < size; i++)
    {
        temp[i] = s.get(start+i);
    }
    return temp;
}

char* concat(MyString &s1, MyString &s2){
    int s1_len = s1.length();
    int s2_len = s2.length();
    int size = s1_len + s2_len;
    char* temp = new char[size];
    for (int i = 0; i < s1_len; i++)
    {
        temp[i] = s1.get(i);
    }
    for (int i = 0; i < s2_len; i++)
    {
        temp[s1_len + i] = s2.get(i);
    }
    return temp;
}
```

## 2. MyString Test

For testing `expand()` function, set `INIT_SIZE = 5, EXPAND_SIZE = 5`.

```c++
//mystring_test.cpp
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
expanded from 5 to 10. 
expanded from 10 to 15.

test string 1

1
1
expanded from 5 to 10.
expanded from 10 to 15.
expanded from 15 to 20.
expanded from 20 to 25.
expanded from 25 to 30.
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
    bool result = mystring::compare(s1, s2);
    std::cout<< result << std::endl;
    char* s3 = mystring::substring(s2, 0, 1);
    std::cout<< s3<<"\n";
    delete [] s3;
    char* s4 = mystring::concat(s1, s2);
    std::cout<< s4<<"\n";
    delete [] s4;
}
/*
test string 1
test string 2
0
te
test string 1test string 2
*/


int main(int argc, char const *argv[])
{
    test1();
    test2();
    return 0;
}

```

## 3. Index Algorithms

### 3.1. Plain Algorithm

```c++
//mystring.h
int index_plain(MyString &string, MyString &pattern){
    for (int i = 0; i <= string.length()-pattern.length(); i++)
    {
        bool flag = true;
        for (int j = 0; j < pattern.length(); j++)
        {
            if(string.get(i + j) == pattern.get(j)){
                continue;
            }else{
                flag = false;
                break;
            }
        }
        if(flag == true)return i;
    }
    return -1;
}
```

### 3.2. KMP Algorithm

```c++
//mystring.h
int index_KMP(MyString &string, MyString &pattern){

    int* next = new int[pattern.length()];
    {
        int i=0,j=-1;
        next[0]=-1;
        while (i < pattern.length()){
            if (j == -1 || pattern.get(i) == pattern.get(j)){
                ++i;
                ++j;
                next[i] = j;
            } else	j = next[j];
        }
    }
    
    std::cout<<"next[] = ";
    for (int i = 0; i < pattern.length(); i++)
    {
        std::cout<<next[i];
    }
    std::cout<<"\n";
    
    for (int i=0,j = 0; i < string.length();)
    {
        if(j == -1 || string.get(i) == pattern.get(j)){
            ++i;
            ++j;
            if(j == pattern.length()){  // matched!
                delete [] next;
                return i-j;
            }
        }else{
            j = next[j];
        }
    }
    delete [] next;
    return -1;
} 
```
### 3.3. Performance Test

For testing, set `INIT_SIZE = 2560000`.

```c++
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

```