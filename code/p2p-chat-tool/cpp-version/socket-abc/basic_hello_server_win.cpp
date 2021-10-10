#include<iostream>
#include<winsock2.h>
#pragma comment(lib, "ws2_32.lib")

using std::cout;

/*
socket编程windows平台基本实现，服务端程序
编译指令：g++ .\hello_server_win.cpp -lwsock32 -o server
*/

int main(int argc, char* argv[]){
    WSADATA wasData;
    SOCKET hServerSock, hClntSock;
    SOCKADDR_IN servAddr, clntAddr;
    int szClntAddr;
    char message[] = "Hello World!";

    if(argc!=2){
        exit(1);
    }

    if(WSAStartup(MAKEWORD(2,2), &wasData) != 0){
        cout<<"WSAStartup() failed!";
    }

    hServerSock = socket(PF_INET, SOCK_STREAM, 0);
    if(hServerSock == INVALID_SOCKET){
        cout<<"socket() error!";
    }

    /*
    关于SOCKADDR_IN、SOCKADDR：
        这两个结构体用来处理套接字所需要的协议、地址、端口等信息，
        struct sockaddr_in{
            sa_family_t     sin_family;  //地址簇
            uint16_t        sin_port;    //16位TCP/UDP端口号 0~65535，0~1023为知名端口号
            struct in_addr  sin_addr;    //32位IP地址
            char            sin_zero[8]; //占位用
        }
        struct in_addr{
            in_addr_t s_addr; //32位IPv4地址
        }
        结构体中使用的数据类型，是POSIX标准额外定义的，为了考虑扩展性
        in_addr_t = uint32_t
        uint16_t = unsigned 16-bit int(unsigned short)
        如此可以保证任何时候int32_t都占用32位4字节，与平台无关

        注意bind函数调用时候的第二个参数：
        bind(hServerSock, (SOCKADDR*) &servAddr->SOCKADDR_IN, sizeof(servAddr))
        引入sockaddr结构体：
        struct sockaddr{
            sa_family_t  sin_family;  // 地址簇
            char         sa_data[14]; // 地址信息，需要包含IP地址及端口号，剩余部分补零
        }
        bind函数的第二个参数希望得到sockaddr结构体变量的地址，sockaddr并非仅针对IPv4设计的，
        所以可以看到sa_data有14个字节，那么手动构建sockaddr结构体就要处理补零等问题，于是乎
        sockaddr_in应运而生，将sockaddr_in的信息填充好，调用bind函数时候进行自动转换即可

    关于htonl、htons：
        CPU有大端序、小端序，数据在不同主机传输过程中，统一使用大端序，称为网络字节序
        htons = h(host=主机字节序) to n(network=网络字节序) short
            把short型数据从主机字节序转换为网络字节序
        htonl = 把long型数据从主机字节序转换为网络字节序
        ntohs、ntohl 同理

        除了如下向sockaddr_in结构体变量填充数据外，无需手动处理字节序问题
    
    关于sin_addr：
        sin_addr为in_addr_t类型，即uint32_t类型，32位整型数据，将IP地址转换为32为二进制数
        很麻烦，可以通过`in_addr_t inet_addr(const char* string)`函数实现转换。
        
        // 通过inet_addr转换后，还需要手动将转换结果存放到sockaddr_in结构体中，
        // 所以可以借助另外一个函数`int inet_aton(const char* string, struct in_addr* addr)`
        // 函数，其会将转换结果直接放到结构体中去。（仅Linux平台，需要头文件<arpa/inet.h>）

        INADDR_ANY：
            创建服务端套接字时候，可以使用INADDR_ANY常数分配IP地址，此种方式可以自动获取计算
            机IP地址。注意是服务端。

    */
    memset(&servAddr, 0, sizeof(servAddr));
    servAddr.sin_family = AF_INET;
    // char addr[] = "127.0.0.1";
    // servAddr.sin_addr.s_addr = inet_addr(addr);
    servAddr.sin_addr.s_addr = htonl(INADDR_ANY);  //win32，win64，linux32平台下，long类型为4字节
    servAddr.sin_port =htons(atoi(argv[1]));       //win32，win64，linux32，linux64位平台下，short类型均为2字节

    /*
    通过bind函数将上面构建的套接字及相关信息绑定在一起，成功返回0，失败返回-1
    */
    if(bind(hServerSock, (SOCKADDR*) &servAddr, sizeof(servAddr)) == SOCKET_ERROR){
        cout<<"bind() error!";
    }

    if(listen(hServerSock, 5) == SOCKET_ERROR){
        cout<<"listen() error!";
    }

    szClntAddr = sizeof(clntAddr);
    hClntSock = accept(hServerSock, (SOCKADDR*) &clntAddr, &szClntAddr);
    if(hClntSock == INVALID_SOCKET){
        cout<<"accept() error";
    }

    send(hClntSock, message, sizeof(message), 0);

    closesocket(hClntSock);
    closesocket(hServerSock);
    WSACleanup();
    return 0;
}