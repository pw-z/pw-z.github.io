#include<string>
#include<iostream>

using std::string;
using std::cout;

string change(string s){
    cout<<"s = "<<s<<"\n";
    char head = s[0];
    cout<<"head(s[0]) = "<<head<<" = "<< (int)head<<"\n";

    for (int i = 0; i < s.length(); ++i)
    {
        cout<<"s["<<i<<"] = "<<s[i]<<", s[i]-head = [";
        int x = ((int)s[i] - (int)head + 26)%26;
        cout<<x<<"]\n";
        s[i] = (char)x + '0';
        // s[i] = 'a';
    }
    return s;
}

int main(int argc, char const *argv[])
{
    string s = change("az");
    cout<<"s = "<<s<<"\n";
    string s2 = change("ba");
    cout<<"s2 = "<<s2<<"\n";
    return 0;
}
