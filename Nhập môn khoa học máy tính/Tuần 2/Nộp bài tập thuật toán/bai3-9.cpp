// Yêu cầu:
// 1. nhập 2 số nguyên dương M, N (M>0 và N>0)
// 2. in ra tổng các số chẵn từ M đến N

#include <iostream>
using namespace std;

// hàm kiểm tra số chẵn
bool KiemTra_SoChan(int thamSo){
    bool khoi_tao;

    if(thamSo % 2 == 0){
        khoi_tao = true;
    }else{
        khoi_tao = false;
    }

    return khoi_tao;
}

// hàm tính tổng các số chẵn
// từ trong khoảng [M, N]
int TinhTong_SoChan(int m, int n){
    int khoi_tao = 0;

    for(int i = m; i <= n; i++){
        if(KiemTra_SoChan(i) == true){
            khoi_tao = khoi_tao + i;
        }
    }

    return khoi_tao;
}

int main(){
    cout << "Nhap 2 so nguyen duong M, N: " << endl;
    int M, N;
    cin >> M >> N;

    while (M <= 0 || N <= 0)
    {
        cout << "Nhap lai M, N: " << endl;
        cin >> M >> N;
    }

    cout << "Ket qua: " << TinhTong_SoChan(M, N);
    cout << endl;

    return 0;
}