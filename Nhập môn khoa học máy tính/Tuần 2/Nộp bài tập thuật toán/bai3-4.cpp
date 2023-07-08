// Yêu cầu:
// 1. nhập tên sản phẩm
// 2. nhập số lượng
// 3. nhập đơn giá
// 4. tính tiền
// 5. tính thuế giá trị gia tăng

// số_tiền = số_lượng * đơn_giá
// thuế = số_tiền * 10 / 100

#include <iostream>
#include <string>
using namespace std;

int main(){
    cout << "Nhap ten san pham: ";
    string tenSP;
    getline(cin, tenSP, '\n');

    cout << "Nhap so luong: ";
    int so_luong;
    cin >> so_luong;

    cout << "Nhap don gia: ";
    int don_gia;
    cin >> don_gia;

    float tien = so_luong * don_gia;
    float thue = tien * 10 / 100;

    cout << "So tien cua san pham \"" << tenSP << "\" la: " << tien << endl;
    cout << "So tien thue la: " << thue << endl;

    return 0;
}