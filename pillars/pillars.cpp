#include <iostream>
#include <stack>

using namespace std;

char pillars(std::string temple_str) {
  stack<char> temple;
  for (char& pillar: temple_str) {
    if(pillar == '(' || pillar == '{' || pillar == '[') {
      temple.push(pillar);
      continue;
    }
    if (temple.empty()) return 'F';
    char last_pillar = temple.top();
    temple.pop();
    if (pillar == ')' && last_pillar == '(' || pillar == '}' && last_pillar == '{' || pillar == ']' && last_pillar == '[') {
      continue;
    }
    return 'F';
  }
  return temple.empty() ? 'T' : 'F';
}

int main() {
  string in;
  cin >> in;
  cout << pillars(in) << endl;
  return 0;
}