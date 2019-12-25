#include <bits/stdc++.h>
using namespace std;

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
  string s;
  vector<string> arr;
  getline(cin, s);

  arr = stov(s);

  for (int i = 0; i < arr.size(); i++) {
    for (int j = 0; j < arr[i].size(); j++) {
      if ((arr[i][j] == 'i') && (arr[i][j + 1] == 'n') && (arr[i][j + 2] == 'g') && (j + 2 == arr[i].size() - 1)) {
        arr[i].replace(j, 3, "ed");
      }
    }
  }

  s = vtos(arr);

  cout << s;

  return 0;
}
