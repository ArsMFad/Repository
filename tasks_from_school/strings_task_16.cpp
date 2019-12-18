#include <bits/stdc++.h>
using namespace std;

vector<string> change(vector<string> arr) {
  string tmp = arr[0];
  arr[0] = arr[arr.size() - 1];
  arr[arr.size() - 1] = tmp;
  return arr;
}

string vtos (vector<string> arr) {
  string s = "";
  string tmp = arr[0];

  for (int i = 0; i < arr.size(); i++) {
    s += arr[i];
  }
  return s;
}

vector<string> stov (string s) {
  vector<string> arr;
  string tmp = "";
  
  for (int i = 0; i < s.size(); i++) {
    if (s[i] == ' ') {
      if(arr.size() != 0) {
        arr.push_back(" ");
        arr.push_back(tmp);
        tmp = "";
      } else {
        arr.push_back(tmp);
        tmp = "";
      }
    } else {
      tmp += s[i];
    }
  }

  arr.push_back(" ");
  arr.push_back(tmp);

  return arr;
}

int main() {
  ios::sync_with_stdio(0);
  cin.tie(0);
  cout.tie(0);

  string arr;
  getline(cin, arr);
  arr.erase(arr.size() - 1, 1);

  if (stov(arr)[0].size() == stov(arr)[stov(arr).size() - 1].size()) {
    cout << vtos(change(stov(arr)));
  } else {
    cout << vtos(stov(arr));
  }

  return 0;
}
