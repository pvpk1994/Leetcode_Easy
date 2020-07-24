// Reverse a string using Recursion

#include <iostream>
#include <string>
using namespace std;

void helper_fn(int index, string& str)
{
  if(index>=str.size() || str.empty())
  {
    return;
  }
  // get to the end of the string
  helper_fn(index+1, str);
  // if here: index points to the end of the string
  if(index <= str.size())
  {
    char elem = str.back();
    str.pop_back();
    int rev_index = str.size()-index;
    // str[rev_index] = elem;
    str.insert(rev_index, 1, elem);
  }

}

void string_reverse(string& str)
{
  int index = 0;
  helper_fn(index, str);

}
int main() {
  //std::cout << "Hello World!\n";
  string given = "pavan kumar";
  string_reverse(given);
  cout << given << endl;
}
