#include "706_design_hashmap.h"
int main(int argc, char const *argv[]){
    MyHashMap* o = new MyHashMap();
    o->put(1,1);
    o->put(2,2);
    o->get(1);
    o->get(3);
    o->put(2,1);
    o->get(2);
    o->remove(2);
    o->get(2);
    return 0;
}