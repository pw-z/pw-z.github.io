#include<winsock2.h>
#include<ws2tcpip.h>
#include<iostream>
#pragma comment(lib, "ws2_32.lib")

using std::cout;
using std::cin;
using std::endl;

#define BUFF_SIZE 1024

/*
Windows平台下socket编程实践
测试平台: windows10
创建时间：2021年10月10日
*/

int main(){
    char username[100];
    char target_addr[33];
    char target_port[17];
    SOCKET req_host_socket, req_clnt_socket,
           res_host_socket, res_clnt_socket;
    SOCKADDR_IN host_addr, clnt_addr;
    char message[BUFF_SIZE];


    cout<<"login with name: ";
    cin>>username;
    cout<<"hello, "<<username<<endl;
    cout<<"target address: ";
    cin>>target_addr;
    cout<<"target port: ";
    cin>>target_port;
    cout<<"socket you input: "<<target_addr<<":"<<target_port<<endl;
    
    /*
    WSAStartup，即WSA(Windows Sockets Asynchronous，Windows异步套接字)
    的启动命令。是Windows下的网络编程接口软件Winsock1 或 Winsock2 里面的
    一个命令（Ps：Winsock 是由Unix下的BSD Socket发展而来,是一个与网络协议
    无关的编程接口）。
    WSAStartup必须是应用程序或DLL调用的第一个Windows Sockets函数。它允许
    应用程序或DLL指明Windows Sockets API的版本号及获得特定Windows Sockets
    实现的细节。应用程序或DLL只能在一次成功的WSAStartup()调用之后才能调用
    进一步的Windows Sockets API函数。初始化成功将返回0，否则将返回错误代码
    
    > https://baike.baidu.com/item/WSAStartup
    */
    WSADATA wsaData;
    if(WSAStartup(MAKEWORD(2,2), &wsaData) != 0){
        cout<<"WSAStartup failed!";
    }

    /*
    套接字创建函数：
    int socket(int domain, int type, int protocol)
        domain：套接字所使用的协议簇
        type：套接字数据传输类型
        protocol：具体使用的通讯协议

    domain：
        INET: IPv4
        INET6: IPv6
        LOCAL: 本地通信的UNIX协议簇
        ...

    type：
        SOCK_STREAM: 可靠的、按序传递的、基于字节的面向连接的数据传输方式的套接字
        SOCK_DGRAM: 不可靠的、不按序传递的、以数据的高速传输为目的的套接字

    protocol：
        前两个参数在大多数情况下已经可以具体确定一个协议，此时直接传递0即可，除非：
        同一协议族中存在多个数据传输方式相同的协议
    
    基于IPv4协议簇下面向连接的协议，只有IPPROTO_TCP
    */
    int server_sock = socket(AF_INET, SOCK_STREAM, IPPROTO_TCP);


    




    cout<<"do something here";

    WSACleanup();  // 终止Winsock2的使用，操作成功返回值为0
    return 0;
}