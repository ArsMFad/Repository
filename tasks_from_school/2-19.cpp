#include <bits/stdc++.h>
using namespace std;

int main() {
  ios::sync_with_stdio(0);
  cin.tie(0);
  cout.tie(0);


  string s;
  vector<int> arr;
  int k, tmp;

  getline(cin, s);

  cin >> k;
  while (k!= 0) {
    arr.push_back(k);
    cin >> k;
  }
  arr.resize(arr.size());

  tmp = arr[0];
  s.insert(tmp, " ");
  for (int i = 1; i < arr.size() - 1; i++) {
    tmp += arr[i] + 1;
    s.insert(tmp, " ");
  }

  cout << s;

  return 0;
}