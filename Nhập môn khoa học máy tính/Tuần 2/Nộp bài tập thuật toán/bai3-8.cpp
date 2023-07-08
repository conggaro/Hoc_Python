// Yêu cầu:
// 1. nhập vào 1 số nguyên N (N >= 0)
// 2. viết hàm tính giai thừa

// cho biết 0! thì bằng 0

#include <iostream>
using namespace std;

// hàm tính giai thừa
int TinhGiaiThua(int thamSo){
    int khoi_tao = 0;

    if(thamSo == 0 || thamSo == 1){
        khoi_tao = 1;
    }else{
        khoi_tao = thamSo * TinhGiaiThua(thamSo - 1);
    }

    return khoi_tao;
}

int main(){
    cout << "Nhap vao 1 so N: ";
    int N;
    cin >> N;

    while (N < 0)
    {
        cout << "Nhap lai N (N >= 0): ";
        cin >> N;
    }
    
    cout << N << "! = " << TinhGiaiThua(N) << endl;

    return 0;
}