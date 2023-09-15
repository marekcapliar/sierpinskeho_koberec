#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int main(){
  int list[] = {-52, 56, 30, 29, -54, 0, -110};
  int len = sizeof(list)/sizeof(list[0])-1;
  vector<int> myvector (list, list + len);
  sort(myvector.begin(), myvector.end());
  for(int i = 0; i <= len + 1; i++){
    cout << myvector[i] << '\n';
  }
  cout << "big: " << list[(len)]<< "\nsize: " << len << '\n';
  return 0;
}