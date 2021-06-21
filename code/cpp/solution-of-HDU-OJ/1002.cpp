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
    char number_a[1000], number_b[1000];
    char number_sum[1001];
    for (int i = 0; i < lines; i++){
        cin>>number_a>>number_b;
        
        cout<<number_a<<" + "<<number_b<<" = "<<number_sum<<endl<<endl;
    }
    
    return 0;
}
