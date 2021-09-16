#include <vector>
#include<iostream>
using std::cout;
using std::vector;
class MyHashMap {
     struct Node
     {
         int key;
         int val;
         Node* next;
     };
     vector<Node*> bucket;
     int BUCKET_SIZE = 1013;
     int hash(int key){
         return key%BUCKET_SIZE;
     }
public:
    /** Initialize your data structure here. */
    MyHashMap() {
        bucket = vector<Node*>(BUCKET_SIZE);
    }

    bool contains(int key){
        int loc = hash(key);
        if(bucket[loc] == nullptr) return false;
        else{
            Node* cur = bucket[loc];
            while (cur != nullptr)
            {
                if (cur->key == key )
                {
                    return true;
                }
                cur = cur->next;
            }
        }
        return false;
    }

    Node* locate(int key){
        int loc = hash(key);
        Node* cur = bucket[loc];
        while (cur != nullptr)
        {
            if (cur->key == key)
            {
                return cur;
            }
            cur = cur->next;
        }
        return nullptr;
    }
    
    /** locate_parent should be used only if contains(key) == true*/
    /** when bucket[loc] hit the key, return nullptr*/
    Node* locate_parent(int key){
        int loc = hash(key);
        Node* cur = bucket[loc];
        if(bucket[loc]->key == key){
            return nullptr;
        }
        while (cur->next != nullptr)
        {
            if (cur->next->key == key)
            {
                return cur;
            }
            cur = cur->next;
        }
        return nullptr;
    }




    void add(int key, int value) {
        int loc = hash(key);
        Node* newnode = new Node;
        newnode->key = key;
        newnode->val = value;
        if (bucket[loc] == nullptr)
        {
            bucket[loc] = newnode;
        }else{
            newnode->next = bucket[loc]->next;
            bucket[loc] = newnode;
        }
    }
    
    /** value will always be non-negative. */
    void put(int key, int value) {
        if(contains(key)){
            Node* cur = locate(key);
            cur->val = value;
        }else{
            add(key, value);
        }
    }
    
    /** Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key */
    int get(int key) {
        if(contains(key)){
            Node* cur = locate(key);
            return cur->val;
        }
        return -1;
    }
    
    /** Removes the mapping of the specified value key if this map contains a mapping for the key */
    void remove(int key) {
        if (contains(key))
        {
            Node* cur = locate_parent(key);
            if (cur != nullptr){
                cur->next = cur->next->next;
                delete cur;
            }else{
                int loc = hash(key);
                delete bucket[loc];
                bucket[loc] = nullptr;
            }
        }
    }
};

/**
 * Your MyHashMap object will be instantiated and called as such:
 * MyHashMap* obj = new MyHashMap();
 * obj->put(key,value);
 * int param_2 = obj->get(key);
 * obj->remove(key);
 */

int main(int argc, char const *argv[])
{
    MyHashMap* obj = new MyHashMap();
    obj->put(1,299);
    int param_2 = obj->get(1);
    cout<<param_2<<"\n";
    obj->remove(1);
    param_2 = obj->get(1);
    cout<<param_2<<"\n";
    return 0;
}
