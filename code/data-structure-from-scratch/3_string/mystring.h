#ifndef MYSTRING_H_
#define MYSTRING_H_

namespace mystring {

static const int INIT_SIZE = 256;
static const int EXPAND_SIZE = 256;


class MyString
{
private:
    char* mystring_;
    int length_;
public:
    MyString();
    MyString(char*);
    ~MyString();
    int length();
    bool isempty();
    bool append(MyString s);
    bool insert(char*);
    void print();
};

MyString::MyString()
{
}

MyString::~MyString()
{
}




/*************not class method**************/

bool compare(MyString s1, MyString s2){}

bool substring(MyString s, int start, int end){}

MyString concat(MyString s1, MyString s2){}

int index_plain(MyString s1, MyString s2){}
int index_KMP(MyString s1, MyString s2){} 

}//namespace mystring

#endif