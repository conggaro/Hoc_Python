// Yêu cầu:
// 1. giải phương trình bậc nhất ax + b = 0
// 2. a và b là số thực

#include <iostream>
#include <iomanip>
using namespace std;

int main(){
    cout << "Nhap vao a: ";
    float a;
    cin >> a;

    while(a == 0){
        cout << "Nhap lai a (a khac 0): ";
        cin >> a;
    }

    cout << "Nhap vao b: ";
    float b;
    cin >> b;

    float x = (0 - b) / a;

    cout << fixed << setprecision(3);
    cout << "Ket qua: " << x << endl;

    return 0;
}