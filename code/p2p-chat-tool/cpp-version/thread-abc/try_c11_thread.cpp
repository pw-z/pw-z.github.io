#include<iostream>
#include<thread>  // c11引入的线程库，，在c14、c17中有更新

using std::cout;
using std::cin;

void hello(){
    cout<<"hello c11 thread\n";
}

void thread_hello(){
    std::thread t(hello);  // 每个线程需要有一个执行单元，此处将hello函数作为线程t的执行单元
    t.join();
}

int main(){
    thread_hello();
}