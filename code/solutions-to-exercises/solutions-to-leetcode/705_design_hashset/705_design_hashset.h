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
            Node* temp = cur;
            while(cur != nullptr){
                if(cur->val == key){
                    if(cur == bucket[hash(key)]){
                        bucket[hash(key)] = cur->next;
                    }else{
                        cur = cur->next;
                    }
                    // delete temp;
                    return;
                }
                cur = cur->next;
                temp = cur;
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


/*
int main(int argc, char const *argv[])
{
    MyHashSet* obj = new MyHashSet();
    obj->add(1);
    obj->add(2);
    bool res = obj->contains(1);
    cout<<res<<"\n";
    res = obj->contains(3);
    cout<<res<<"\n";
    obj->add(2);
    res = obj->contains(2);
    cout<<res<<"\n";
    obj->remove(2);
    res = obj->contains(2);
    cout<<res<<"\n";
    return 0;
}
*/