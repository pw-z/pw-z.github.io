#include <vector>
#include <iostream>

using std::vector;
using std::cout;

class MyHashSet {
public:
    /** Initialize your data structure here. */
    struct Node{
        int val;
        Node* next;
    };
    vector<Node*> bucket;

    MyHashSet() {
        bucket = vector<Node*>(1013);
    }
    
    int hash(int num){
        return num%1013;
    }

    void add(int key) {
        if(contains(key)) return;
        int loc = hash(key);
        Node* temp = new Node();
        temp->val = key;
        if(bucket[loc] == nullptr){
            bucket[loc] = temp;
        }else{
            temp->next = bucket[loc];
            bucket[loc] = temp;
        }
    }
    
    void remove(int key) {
        
        if(bucket[hash(key)] != nullptr){
            Node* cur = bucket[hash(key)];
            bucket[hash(key)] = nullptr;
            Node* temp;
            while(cur != nullptr){
                temp = cur;
                cur = cur->next;
                delete temp;
            }
        }
    }
    
    /** Returns true if this set contains the specified element */
    bool contains(int key) {
        int loc = hash(key);
        if(bucket[loc] != nullptr){
            Node* cur = bucket[loc];
            while(cur != nullptr){
                if(cur->val == key){
                    return true;
                }
                cur = cur->next;
            }
        }
        return false;
    }
};

/**
 * Your MyHashSet object will be instantiated and called as such:
 * MyHashSet* obj = new MyHashSet();
 * obj->add(key);
 * obj->remove(key);
 * bool param_3 = obj->contains(key);
 */



// int main(int argc, char const *argv[])
// {
//     MyHashSet* obj = new MyHashSet();
//     obj->add(1234);
//     bool res = obj->contains(1234);
//     cout<<res<<"\n";
//     obj->remove(1234);
//     bool res2 = obj->contains(1234);
//     cout<<res2<<"\n";
//     obj->remove(12344);
//     return 0;
// }
