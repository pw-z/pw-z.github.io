#include <iostream>
using namespace std;

/**
 * not that simple
 */
int try1() {
    int lines;
    cin >> lines;
    long long A, B;
    for (int i = 0; i < lines; i++) {
        cin >> A >> B;
        cout << "Case " << i + 1 << ":" << endl;
        cout << A << " + " << B << " = " << A + B << endl << endl;
    }
    return 0;
}

/**
 * find out whats in char* after cin>>char*
 */
int try2() {
    int lines;
    cin >> lines;
    char number_a[20], number_b[20];
    char number_sum[1001];
    for (int i = 0; i < lines; i++) {
        cin >> number_a >> number_b;

        // cout<< sizeof(number_a) << sizeof(number_b) << endl;
        cout << number_a << " + " << number_b << " = "
             << "number_sum" << endl
             << endl;
        cout << "number_a: ";
        for (int i = 0; i < 20; i++) {
            if (number_a[i] == '\0') {
                cout << "$";
            } else if (number_a[i] < 48 || number_a[i] > 57) {
                cout << "_";
            } else {
                cout << number_a[i];
            }
        }
        cout << endl;
        cout << "number_b: ";
        for (int i = 0; i < 20; i++) {
            if (number_b[i] == '\0') {
                cout << "$";
            } else if (number_b[i] < 48 || number_b[i] > 57) {
                cout << "_";
            } else {
                cout << number_b[i];
            }
        }
        cout << endl;

        // cout<<number_a<<" + "<<number_b<<" = "<<number_sum<<endl<<endl;
    }
    return 0;
}
/*terminal
2
123456 22223333
123456 + 22223333 = number_sum

number_a: 123456$$___$$$$$_$$$
number_b: 22223333$$$$$$$$$$$$
45646 8979879
45646 + 8979879 = number_sum

number_a: 45646$$$___$$$$$_$$$
number_b: 8979879$$$$$$$$$$$$$
*/

int try3() {
    int lines;
    cin >> lines;
    char number_a[1000], number_b[1000];
    char number_sum[1001];
    for (int i = 0; i < lines; i++) {
        cin >> number_a >> number_b;
        // number_a['1', '1', '\0',...]
        // number_b['1', '1', '3', '\0',...]
        int length_a, length_b;
        for (int i = 0; i < 1000; i++) {
            if (number_a[i] == '\0') {
                length_a = i;
                break;
            }
        }
        for (int i = 0; i < 1000; i++) {
            if (number_b[i] == '\0') {
                length_b = i;
                break;
            }
        }
        cout << "length_a = " << length_a << "\nlength_b = " << length_b
             << endl;

        for (int i = 0; i < length_a; i++) {
            cout << number_a[i];
        }
        cout << endl;
        for (int i = 0; i < length_b; i++) {
            cout << number_b[i];
        }
        cout << endl;

        for (int i = length_a; i >= 0; --i) {
            cout << number_a[i];
        }
        cout << endl;
        for (int i = length_b; i >= 0; --i) {
            cout << number_b[i];
        }
        cout << endl;

        // cout<<number_a<<" + "<<number_b<<" = "<<number_sum<<endl<<endl;
    }
    return 0;
}

/**
 * in a mess.
 */
int try4() {
    int lines;
    cin >> lines;
    char number_a[1000], number_b[1000];
    char number_sum[1001];
    for (int i = 0; i < lines; i++) {
        cin >> number_a >> number_b;
        // number_a['1', '1', '\0',...]
        // number_b['1', '1', '3', '\0',...]
        int length_a, length_b;
        for (int i = 0; i < 1000; i++) {
            if (number_a[i] == '\0') {
                length_a = i;
                break;
            }
        }
        for (int i = 0; i < 1000; i++) {
            if (number_b[i] == '\0') {
                length_b = i;
                break;
            }
        }
        cout << "length_a = " << length_a << "\nlength_b = " << length_b
             << endl;

        for (int i = length_a; i >= 0; --i) {
            cout << number_a[i];
        }
        cout << endl;
        for (int i = length_b; i >= 0; --i) {
            cout << number_b[i];
        }
        cout << endl;

        int flag = 0, temp_a, temp_b;
        for (int i = length_a - 1, j = length_b - 1, k = 0;; --i, --j, ++k) {
            if (i < 0) {
                temp_a = 0;
            } else {
                temp_a = number_a[i] - '0';
            }
            if (j < 0) {
                temp_b = 0;
            } else {
                temp_b = number_b[j] - '0';
            }
            if ((i <= 0 && j <= -1) || (i <= -1 && j <= 0) ||
                (i <= -1 && j <= -1)) {
                cout << number_sum << endl;
                for (k += 1; k >= 0; --k) {
                    cout << number_sum[k];
                }
                cout << endl << endl;
                break;
            } else {
                number_sum[k] = (temp_a + temp_b + flag) % 10 + '0';
                if ((temp_a + temp_b) > 10) {
                    flag = 1;
                } else {
                    flag = 0;
                }
            }
        }

        // cout<<number_a<<" + "<<number_b<<" = "<<number_sum<<endl<<endl;
    }
    return 0;
}

/**
 * first AC.
 */
int solution1() {
    int lines;
    cin >> lines;
    char number_a[1000], number_b[1000];
    char number_sum[1001];
    for (int i = 0; i < lines; i++) {
        cin >> number_a >> number_b;

        int length_a, length_b;
        for (int i = 0; i < 1000; i++) {
            if (number_a[i] == '\0') {
                length_a = i;
                break;
            }
        }
        for (int i = 0; i < 1000; i++) {
            if (number_b[i] == '\0') {
                length_b = i;
                break;
            }
        }
        // cout << "length_a = " << length_a << "\nlength_b = " << length_b <<
        // endl;

        int length = length_a >= length_b ? length_a : length_b;
        int a, b, flag = 0;
        for (int i = 0; i <= length; ++i) {
            if (i >= length_a) {
                a = 0;
            } else {
                a = number_a[length_a - i - 1] - '0';
            }
            if (i >= length_b) {
                b = 0;
            } else {
                b = number_b[length_b - i - 1] - '0';
            }
            number_sum[i] = ((a + b + flag) % 10) + '0';
            flag = a + b + flag >= 10 ? 1 : 0;
        }
        cout << "Case " << i + 1 << ":\n";
        cout << number_a << " + " << number_b << " = ";
        if (number_sum[length] == '1')
            cout << '1';
        for (int i = 0; i < length; ++i) {
            cout << number_sum[length - i - 1];
        }
        cout << endl;

        if (i + 1 < lines) {  // Output a blank line **between** two test cases.
            cout << endl;
        }
    }
    return 0;
}

int main(int argc, char const* argv[]) {
    // try1();
    // try2();
    // try3();
    // try4();
    solution1();
    return 0;
}
