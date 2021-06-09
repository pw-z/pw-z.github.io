#include <iostream>
using namespace std;


/**
 * Wrong answer, not that simple
 */
// int main(int argc, char const *argv[]){
//     int lines;
//     cin>>lines;
//     long long A,B;
//     for (int i = 0; i < lines; i++)
//     {
//         cin>>A>>B;
//         cout<<"Case "<<i+1<<":"<<endl;
//         cout<<A<<" + "<<B<<" = "<<A+B<<endl<<endl;
//     }
//     return 0;
// }

int main(int argc, char const *argv[])
{
    int lines;
    cin>>lines;
    char number_a[100], number_b[100];
    char number_sum[101];
    for (int i = 0; i < lines; i++){
        cin>>number_a>>number_b;
        for (int i = 100; i >= 0; i--){
            cout<<number_a[i];
            // if (number_a[i] != '\0' || number_b[i] != '\0'){
            //     cout<<number_a[i]+number_b[i]<<endl;
            //     // number_sum[i]  // code 048~057 is ACSII 0~9
            // }
            
        }
        
        cout<<number_a<<" + "<<number_b<<" = "<<number_sum<<endl<<endl;
    }
    
    return 0;
}
