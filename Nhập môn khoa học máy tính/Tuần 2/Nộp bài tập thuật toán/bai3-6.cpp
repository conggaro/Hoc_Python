// Yêu cầu:
// 1. nhập 3 số thực a, b, c
// 2. kiểm tra 3 số có phải độ dài của 3 cạnh tam giác không

#include <iostream>
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

    if(KiemTra_3_canh(a, b, c) == true){
        cout << "a, b, c la do dai 3 canh cua 1 tam giac.";
        cout << endl;
    }else{
        cout << "a, b, c khong phai do dai 3 canh cua 1 tam giac.";
        cout << endl;
    }

    return 0;
}
