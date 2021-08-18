#ifndef _SORT_H_
#define _SORT_H_

#include <iostream>

namespace pwz {

void test_sort(int *data){
    //数组作为函数参数传递后，退化为指针
    std::cout<<sizeof(data)<<"\n";
    
    std::cout<<sizeof(data[0])<<"\n";
    int size = sizeof(data) / sizeof(data[0]);
    std::cout<<"length = "<<size<<"\n";
}


}



#endif