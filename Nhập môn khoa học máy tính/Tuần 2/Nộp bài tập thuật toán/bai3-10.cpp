// Yêu cầu:
// 1. nhập vào 1 số n
// 2. tạo vector v1 có độ dài n
// 3. nhập n số nguyên cho cái v1
// 4. đưa ra giá trị lớn nhất
// 5. đếm xem có số nào trùng với cái số lớn nhất đấy không

#include <iostream>
#include <vector>
using namespace std;

// hàm trả về số lớn nhất trong vector
int SoLonNhat(vector<int> v){
    int max = 0;

    for (int i = 0; i < v.size(); i++)
    {
        if(max < v[i]){
            max = v[i];
        }
    }    

    return max;
}

// hàm đếm xem có mấy giá trị lớn nhất
// kiểu 2 số nó bị trùng nhau
int Dem_Max(vector<int> v){
    int dem = 0;

    // tìm ra số lớn nhất
    int max = SoLonNhat(v);

    // tìm xong rồi thì bắt đầu đếm
    for(int i = 0; i < v.size(); i++){
        if(max == v[i]){
            dem = dem + 1;
        }
    }

    return dem;
}

int main(){
    cout << "Nhap vao so nguyen duong n: ";
    int n;
    cin >> n;

    while (n <= 0)
    {
        cout << "Nhap lai n: ";
        cin >> n;
    }
    
    vector<int> v1(n);

    for(int i = 0; i < v1.size(); i++){
        cout << "Nhap gia tri cho v1[" << i <<"] = ";
        cin >> v1.at(i);
    }

    cout << "So lon nhat la: " << SoLonNhat(v1) << endl;
    cout << "So luong so lon nhat xuat hien trong day la: ";
    cout << Dem_Max(v1) << endl;

    return 0;
}