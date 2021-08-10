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

static const int INIT_SIZE = 2560000;
static const int EXPAND_SIZE = 2560000;

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

/*************not class method**************/
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
/*************not class method**************/



}//namespace mystring

#endif