#include<iostream>
#include<winsock2.h>
#pragma comment(lib, "ws2_32.lib")
#define BUFF_SIZE 1024
using std::cout;
using std::cin;

int main(int argc, char* argv[]){
    WSADATA wasData;
    SOCKET hSocket;
    SOCKADDR_IN servAddr;
    int szClntAddr;
    char message[BUFF_SIZE];
    int str_len, recv_len, recv_cnt;

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

    while(1){
        cout<<"before input, strlen message: "<<strlen(message)<<"\n";
        cin>>message;
        cout<<"after input, strlen message: "<<strlen(message)<<"\n";
        cout<<"your input: "<<message<<"\n";

        if(!strcmp(message, "q") || !strcmp(message, "Q")){
            break;
        }
        str_len = send(hSocket, message, strlen(message), 0);

        recv_len = 0;
        while(recv_len < str_len){  // 循环将所发送出去的消息读取完整
            recv_cnt = recv(hSocket, message, BUFF_SIZE-1, 0);
            if(recv_cnt == -1){
                cout<<"read() error!";
            }
            cout<<"recv_cnt = "<<recv_cnt<<"\n";
            recv_len += recv_cnt;
        }
        message[recv_len] = 0; // 确定字符串结束位置
        cout<<"server echo:\n"<<message<<"\n";
        memset(message, 0, sizeof(message));
    }
    
    closesocket(hSocket);
    WSACleanup();
    return 0;
}