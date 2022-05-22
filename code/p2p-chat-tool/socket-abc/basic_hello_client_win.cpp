#include<iostream>
#include<winsock2.h>
#pragma comment(lib, "ws2_32.lib")

using std::cout;

/*
socket编程windows平台基本实现，客户端程序
编译指令：g++ .\hello_client_win.cpp -lwsock32 -o client
*/
int main(int argc, char* argv[]){
    WSADATA wasData;
    SOCKET hSocket;
    SOCKADDR_IN servAddr;
    int szClntAddr;
    char message[30];
    int strlen;

    if(argc!=3){
        exit(1);
    }

    if(WSAStartup(MAKEWORD(2,2), &wasData) != 0){
        cout<<"WSAStartup() failed!";
    }

    hSocket = socket(PF_INET, SOCK_STREAM, 0);
    if(hSocket == INVALID_SOCKET){
        cout<<"socket() error!";
    }

    memset(&servAddr, 0, sizeof(servAddr));
    servAddr.sin_family = AF_INET;
    servAddr.sin_addr.s_addr = inet_addr(argv[1]);
    servAddr.sin_port =htons(atoi(argv[2]));

    if(connect(hSocket, (SOCKADDR*) &servAddr, sizeof(servAddr)) == SOCKET_ERROR){
        cout<<"connect() error!";
    }

    strlen = recv(hSocket, message, sizeof(message-1), 0);
    if(strlen == -1){
        cout<<"read() error!";
    }
    cout<<"message from server:\n"<<message;

    closesocket(hSocket);
    WSACleanup();
    return 0;
}