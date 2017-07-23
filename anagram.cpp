#include <map>
#include <set>
#include <list>
#include <vector>
#include <iostream>

/*
 * Alice is taking a cryptography class and finding anagrams to be very useful. We consider two strings to be anagrams of each other if the first string's letters can be rearranged to form the second string. In other words, both strings must contain the same exact letters in the same exact frequency For example, bacdc and dcbac are anagrams, but bacdc and dcbad are not.

Alice decides on an encryption scheme involving two large strings where encryption is dependent on the minimum number of character deletions required to make the two strings anagrams. Can you help her find this number?

Given two strings,  and , that may or may not be of the same length, determine the minimum number of character deletions required to make  and  anagrams. Any characters can be deleted from either of the strings.

This challenge is also available in the following translations:

Chinese
Russian
Input Format

The first line contains a single string, . 
The second line contains a single string, .

Constraints

It is guaranteed that  and  consist of lowercase English alphabetic letters (i.e.,  through ).
Output Format

Print a single integer denoting the number of characters you must delete to make the two strings anagrams of each other.

Sample Input

cde
abc
Sample Output

4
Explanation

We delete the following characters from our two strings to turn them into anagrams of each other:

Remove d and e from cde to get c.
Remove a and b from abc to get c.
We must delete  characters to make both strings anagrams, so we print  on a new line.
 */
using namespace std;

int number_needed(string a, string b) {
  std::map<char, int> map_a;
  std::map<char, int> map_b;
  int output = 0;
  for (auto it = a.begin(); it != a.end(); ++it) {
    map_a[*it] = map_a[*it] + 1;
  }
  for (auto it = b.begin(); it != b.end(); ++it) {
    map_b[*it] = map_b[*it] + 1;
  }
  for (const auto& it_a : map_a) {
    if (map_b.find(it_a.first) != map_b.end()) {
      // if char is available in both strings.
      output += abs(it_a.second - map_b[it_a.first]);
    } else {
      // when char is available only in first string.
      output += it_a.second;
    }
  }
  for (const auto& it_b : map_b) {
    if (map_a.find(it_b.first) == map_a.end()) {
      // when char is available only in second string.
      output += it_b.second;
    }
  }
  return output;
}

int number_needed_v2(const string &a, const string& b) {
  int output = 0;
  std::vector<int> freq(26, 0);
  for (const auto &c : a) { ++freq[c - 'a']; }
  for (const auto &c : b) { --freq[c - 'a']; }
  for (const auto &c : freq) { count += abs(c); }
  return output;
}

int main(){
    string a;
    cin >> a;
    string b;
    cin >> b;
    cout << number_needed_v2(a, b) << endl;
    return 0;
}
