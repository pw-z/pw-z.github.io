#include<string>
#include<iostream>
#include<unordered_map>
#include<vector>
using namespace std;

class ValidWordAbbr {
    unordered_map<string, string> s2abbr;
    unordered_map<string, vector<string>> abbr2counts;
    string get_abbr(string s){
        if(s.size() < 3){
            return s;
        }else{
            int mid = s.size()-2;
            string abbr = s[0] + to_string(mid) + s[s.size()-1];
            return abbr;
        }
    }
public:
    ValidWordAbbr(vector<string>& dictionary) {
        string abbr_temp;
        for(string s: dictionary){
            abbr_temp = get_abbr(s);
            // cout<<s<<" --> "<<abbr_temp<<endl;
            // s2abbr[s] = abbr_temp;
            abbr2counts[abbr_temp].push_back(s);
        }
        for(auto &it: abbr2counts){
            cout<<it.first<< ": ";
            for(string s: it.second){
                cout<< s<<" ";
            }
            cout<<endl;
        }


    }
    
    bool isUnique(string word) {
        string abbr = get_abbr(word);
        if(abbr2counts.count(abbr) > 0){
            for(string s: abbr2counts[abbr]){
                // cout<<"-----------"<<s;
                if(s != word) return false;
            }
        }
        return true;
    }
};

/**
 * Your ValidWordAbbr object will be instantiated and called as such:
 * ValidWordAbbr* obj = new ValidWordAbbr(dictionary);
 * bool param_1 = obj->isUnique(word);
 */

int main(int argc, char const *argv[])
{
    vector<string> dict = {"deer", "door", "cake", "card"};
    ValidWordAbbr* obj = new ValidWordAbbr(dict);
    cout<< obj->isUnique("dear");
    cout<< obj->isUnique("cart");
    cout<< obj->isUnique("cane");
    cout<< obj->isUnique("make");
    cout<< obj->isUnique("cake");
    return 0;
}
