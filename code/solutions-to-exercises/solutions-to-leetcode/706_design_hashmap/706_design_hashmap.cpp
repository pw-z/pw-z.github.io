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
     int BUCKET_SIZE = 3;
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
        if(bucket[loc] != nullptr){
            Node* cur = bucket[loc];
            while (cur != nullptr){
                if (cur->key == key ){
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
        while (cur != nullptr){
            if (cur->key == key){
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
        while (cur->next != nullptr){
            if (cur->next->key == key){
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
        newnode->next = nullptr;  // !!!
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
            // Node* cur = locate_parent(key);
            int loc = hash(key);
            Node* cur = bucket[loc];
            if(bucket[loc]->key == key){
                delete bucket[loc];
                bucket[loc] = nullptr;
            }else{
                while (cur->next != nullptr){
                    if (cur->next->key == key){
                        cur->next = cur->next->next;
                        delete cur->next;
                        break;
                    }
                    cur = cur->next;
                }
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
    obj->remove(1);
    obj->put(1,299);
    obj->remove(1);
    int param_2 = obj->get(1);
    obj->remove(1);
    param_2 = obj->get(1);
    obj->remove(1);
    obj->remove(1);
    obj->put(1,399);
    obj->put(1,299);
    obj->put(1,499);
    param_2 = obj->get(1);
    obj->remove(1);
    
    return 0;
}
