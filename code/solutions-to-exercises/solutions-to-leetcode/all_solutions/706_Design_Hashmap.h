#include<vector>
using std::vector;

class MyHashMap {
    struct Node
    {
        int k;
        int v;
        Node* next;
        // c++ 支持结构体构造函数
        Node(): k(), v(), next(){}
        Node(int key, int val, Node* next): k(key), v(val), next(next){}
    };
    vector<Node*> bucket;
    int CAPACITY = 3;
    int hash(int key){
        return key%CAPACITY;
    }
    
public:
    /** Initialize your data structure here. */
    MyHashMap() {
        bucket = vector<Node*>(CAPACITY);
    }
    
    /** value will always be non-negative. */
    void put(int key, int value) {
        int loc = hash(key);
        Node* new_node = new Node(key, value, nullptr);
        // temp->k = key;
        // temp->v = value;
        // temp->next = nullptr;

        if (bucket[loc] == nullptr){
            bucket[loc] = new_node;
        }else{

            // if contains(key), update val
            Node* temp = bucket[loc];
            while (temp != nullptr){
                if (temp->k == key){
                    temp->v = value;
                    return;
                }
                temp = temp->next;
            }

            // if not, add new node before head node
            new_node->next = bucket[loc];
            bucket[loc] = new_node;
        }
    }
    
    /** Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key */
    int get(int key) {
        int loc = hash(key);
        if(bucket[loc] == nullptr){
            return -1;
        }else{
            Node* temp = bucket[loc];
            while (temp != nullptr){
                if (temp->k == key){
                    return temp->v;
                }
                temp = temp->next;
            }
            return -1;
        }
    }
    
    /** Removes the mapping of the specified value key if this map contains a mapping for the key */
    void remove(int key) {
        int loc = hash(key);
        if (bucket[loc] == nullptr){
            return;
        }else{

            // handle the first node
            if (bucket[loc]->k == key)
            {
                Node* temp = bucket[loc];
                bucket[loc] = bucket[loc]->next;
                delete temp;
                return;
            }

            // start processing
            Node* pre = bucket[loc];
            Node* cur = pre->next;
            while (cur != nullptr)
            {
                if (cur->k == key)
                {
                    pre->next = cur->next;
                    delete cur;
                    return;
                }
                pre = cur;
                cur = cur->next;
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