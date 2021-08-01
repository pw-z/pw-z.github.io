#ifndef MYSTRING_H_
#define MYSTRING_H_

#include<iostream>

namespace mystring {


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
    }
public:
    MyString();
    MyString(char*);
    ~MyString();
    int length();
    bool isempty();
    bool append(char* s);
    bool remove(int start, int end);
    bool clear();
    void print();
};

MyString::MyString()
{
    mystring_ = new char [INIT_SIZE];
}

MyString::MyString(char* s){
    mystring_ = new char[INIT_SIZE];
    this->append(s);
}

MyString::~MyString()
{
    delete [] mystring_;
}

bool MyString::append(char* s){
    int string_size = strlen(s);
    while(length_ + string_size > capacity_){
        expand();
    }
    for (int i = 0; i < string_size; i++)
    {
        mystring_[length_ + i] = s[i];
    }
    length_ += string_size;
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
}

void MyString::print(){
    for (int i = 0; i < length_; i++)
    {
        std::cout<<mystring_[i];
    }
    std::cout<<"\n";
}

/*************not class method**************/
int strlen(char* s){
    int count = 0;
    while (s[count] != '\0')
    {
        count++;
    }
    return count;
}

bool compare(MyString s1, MyString s2){}
bool substring(MyString s, int start, int end){}
MyString concat(MyString s1, MyString s2){}
int index_plain(MyString s1, MyString s2){}
int index_KMP(MyString s1, MyString s2){} 
/*************not class method**************/



}//namespace mystring

#endif