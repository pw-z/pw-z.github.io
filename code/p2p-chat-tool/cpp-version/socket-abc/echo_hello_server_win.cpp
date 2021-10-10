#include<iostream>
#include<winsock2.h>
#pragma comment(lib, "ws2_32.lib")
#define BUFF_SIZE 1024
using std::cout;

int main(int argc, char* argv[]){
    WSADATA wasData;
    SOCKET hServerSock, hClntSock;
    SOCKADDR_IN servAddr, clntAddr;
    int szClntAddr;
    char message[BUFF_SIZE];
    int strlen;

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

    
    memset(&servAddr, 0, sizeof(servAddr));
    servAddr.sin_family = AF_INET;
    servAddr.sin_addr.s_addr = htonl(INADDR_ANY);
    servAddr.sin_port =htons(atoi(argv[1]));

    if(bind(hServerSock, (SOCKADDR*) &servAddr, sizeof(servAddr)) == SOCKET_ERROR){
        cout<<"bind() error!";
    }

    if(listen(hServerSock, 5) == SOCKET_ERROR){
        cout<<"listen() error!";
    }

    szClntAddr = sizeof(clntAddr);

    for(int i=0; i<5; ++i){
        hClntSock = accept(hServerSock, (SOCKADDR*) &clntAddr, &szClntAddr);
        if(hClntSock == INVALID_SOCKET){
            cout<<"accept() error";
        }else{
            cout<<"client "<<i<<" connected.\n";
        }

        while((strlen = recv(hClntSock, message, BUFF_SIZE, 0)) != 0){
            cout<<"strlen = "<<strlen<<"\n";
            message[strlen] = 0;
            cout<<"client message: "<<message<<"\n";
            send(hClntSock, message, strlen, 0);
        }
        closesocket(hClntSock);
    }

    closesocket(hServerSock);
    WSACleanup();
    return 0;
}