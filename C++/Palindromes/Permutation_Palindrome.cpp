// Permutation Palindrome 
// Author: Pavan Kumar Paluri
// Time Complexity: O(N) and Space: O(1) - [Only a hashmap of 26 characters is possible as there are only limited set of chars]
// Leetcode Question: https://leetcode.com/problems/palindrome-permutation/solution/

class Solution {
public:
    bool canPermutePalindrome(string s) {
        // Create an unordered map
        unordered_map<char,int>h_map;
        for(int i=0; i<s.size(); i++)
        {
            h_map[s[i]]++;
        }
        int counter = 0;
        for(auto iter:h_map)
        {
            counter += iter.second%2;
        }
        if(counter==0 || counter ==1)
            return true;
        else
            return false;
    }
};
