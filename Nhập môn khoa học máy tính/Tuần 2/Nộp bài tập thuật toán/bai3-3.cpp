// Yêu cầu:
// 1. nhập điểm thi
// 2. nhập điểm hệ số 3 (điểm hệ số 3 cũng là điểm thi luôn mà)

#include <iostream>
#include <iomanip>
using namespace std;

int main(){
    cout << "Nhap diem toan: ";
    int d_toan;
    cin >> d_toan;

    cout << "Nhap diem ly: ";
    int d_ly;
    cin >> d_ly;

    cout << "Nhap diem hoa: ";
    int d_hoa;
    cin >> d_hoa;

    float TB = float(d_toan + d_ly + d_hoa) / 3;
    cout << fixed << setprecision(2);
    cout << "Diem TB cua hoc sinh la: " << TB << endl;

    return 0;
}