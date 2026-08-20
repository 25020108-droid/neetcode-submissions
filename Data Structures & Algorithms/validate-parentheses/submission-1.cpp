#include <iostream>
#include <string>
#include <stack>
#include <unordered_map>

using namespace std;

class Solution {
public:
    bool isValid(string s) {
        unordered_map<char, char> brackets = {
            {')', '('},
            {'}', '{'},
            {']', '['}
        };
        
        stack<char> opens;

        for (char c : s) {
            if (brackets.count(c)) { 
                if (opens.empty() || opens.top() != brackets[c]) {
                    return false;
                }
                opens.pop(); 
            } 
            else { 
                opens.push(c);
            }
        }
        return opens.empty(); 
    }
};