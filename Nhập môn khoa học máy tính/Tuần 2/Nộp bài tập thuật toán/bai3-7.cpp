// Yêu cầu:
// 1. nhập 3 số thực a, b, c
// 2. kiểm tra 3 số có phải 3 cạnh của tam giác vuông không

#include <iostream>
#include <cmath>
using namespace std;

// hàm kiểm tra 3 cạnh của 1 tam giác
bool KiemTra_3_canh(float c1, float c2, float c3){
    bool khoi_tao;
    if(c1>0 && c2>0 && c3>0 && (c1+c2)>c3 && (c2+c3)>c1 && (c1+c3)>c2){
        khoi_tao = true;
    }else{
        khoi_tao = false;
    }

    return khoi_tao;
}

// hàm kiểm tra tam giác vuông
void KiemTra_TamGiacVuong(float c1, float c2, float c3){
    if(KiemTra_3_canh(c1, c2, c3) == true){
        cout << "a, b, c la do dai 3 canh cua 1 tam giac.";
        cout << endl;

        bool kiemTra1 = pow(c1, 2) + pow(c2, 2) == pow(c3, 2) ? true : false;
        bool kiemTra2 = pow(c1, 2) + pow(c3, 2) == pow(c2, 2) ? true : false;
        bool kiemTra3 = pow(c2, 2) + pow(c3, 2) == pow(c1, 2) ? true : false;

        if(kiemTra1 == true){
            cout << "La tam giac vuong.";
            cout << endl;
        }else if(kiemTra2 == true){
            cout << "La tam giac vuong.";
            cout << endl;
        }else if(kiemTra3 == true){
            cout << "La tam giac vuong.";
            cout << endl;
        }else{
            cout << "Khong phai tam giac vuong.";
            cout << endl;
        }
    }else{
        cout << "a, b, c khong phai do dai 3 canh cua 1 tam giac.";
        cout << endl;
    }
}

int main(){
    cout << "Nhap vao a: ";
    float a;
    cin >> a;

    cout << "Nhap vao b: ";
    float b;
    cin >> b;

    cout << "Nhap vao c: ";
    float c;
    cin >> c;

    KiemTra_TamGiacVuong(a, b, c);
    return 0;
}