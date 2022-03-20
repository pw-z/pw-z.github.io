#include<iostream>
#include<string>
using std::string;
using std::cout;

int main(int argc, char const *argv[])
{
    // cout<<'a'<<"\n";
    // cout<<'a'-'a'<<"\n";
    // cout<<'c'-'a'<<"\n";
    // cout<<'d'-'b'<<"\n";

    string s1 = "abc";
    string s2 = "bcd";
    cout<<s1<<"\n";
    for (int i = 0; i < s1.length(); i++)
    {
        // s1[i] -= s1[0];
        cout<<s1[i]-'a'<<"\n";
        s1[i] = s1[i] - 'a';
    }
    cout<<s1<<"\n";
    
    return 0;
}
