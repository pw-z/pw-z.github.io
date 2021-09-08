#include <ctime>
#include <iostream>
#include "linearlist.h"
#include "linkedlist.h"

void test_linearlist_insert_time_best_situation(int amount) {
    using namespace linear;
    List<int> mylist = List<int>();
    clock_t start, end;
    start = clock();
    for (int i = 0; i < amount; i++) {
        mylist.insert(i+1, i);
    }
    // mylist.printlist();
    end = clock();
    std::cout<<"linearlist insert "<< amount << " items best  situation cost time: " << end - start << std::endl;
}

void test_linearlist_insert_time_worst_situation(int amount) {
    using namespace linear;
    List<int> mylist = List<int>();
    clock_t start, end;
    start = clock();
    for (int i = 0; i < amount; i++) {
        mylist.insert(1, i);
    }
    // mylist.printlist();
    end = clock();
    std::cout<<"linearlist insert "<< amount << " items worst situation cost time: " << end - start << std::endl;
}

void test_linkedlist_insert_time_best_situation(int amount){
    using namespace linked;
    List<int> mylist = List<int>();
    clock_t start, end;
    start = clock();
    for (int i = 0; i < amount; i++) {
        mylist.insert(1, i);
    }
    end = clock();
    std::cout<<"linkedlist insert "<< amount << " items best  situation cost time: " << end - start << std::endl;
}

void test_linkedlist_insert_time_worst_situation(int amount){
    using namespace linked;
    List<int> mylist = List<int>();
    clock_t start, end;
    start = clock();
    for (int i = 0; i < amount; i++) {
        mylist.insert(i+1, i);
    }
    end = clock();
    std::cout<<"linkedlist insert "<< amount << " items worst situation cost time: " << end - start << std::endl;
}



int main(int argc, char const* argv[]) {

    test_linearlist_insert_time_best_situation(100000);
    test_linearlist_insert_time_worst_situation(100000);
    test_linkedlist_insert_time_best_situation(100000);
    test_linkedlist_insert_time_worst_situation(100000);
   
    test_linearlist_insert_time_best_situation(1000000);
    test_linearlist_insert_time_worst_situation(1000000);
    test_linkedlist_insert_time_best_situation(1000000);
    test_linkedlist_insert_time_worst_situation(1000000);


    return 0;
}

/*
linearlist insert 100000 items best  situation cost time: 1
linearlist insert 100000 items worst situation cost time: 9013
linkedlist insert 100000 items best  situation cost time: 223
linkedlist insert 100000 items worst situation cost time: 20656
linearlist insert 1000000 items best  situation cost time: 10
linearlist insert 1000000 items worst situation cost time: 902397
linkedlist insert 1000000 items best  situation cost time: 2456
linkedlist insert 1000000 items worst situation cost time: 2873597
*/
