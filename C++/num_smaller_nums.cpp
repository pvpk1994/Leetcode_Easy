// How Many Numbers Are Smaller Than the Current Number
// Author: Pavan Kumar Paluri
// Question: https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/

class Solution {
public:
    vector<int> smallerNumbersThanCurrent(vector<int>& nums) {
        // Store in a temp nums
        vector<int>old_nums = nums;
        sort(nums.begin(), nums.end());
        map<int, int>counter;
        for(int i=0;i<nums.size(); i++)
        {
            // Load the hashmap - Counter eq in python 
            counter[nums[i]]++;
        }
        int ans =0;
        map<int, int>new_counter;
        for(const auto &m:counter)
        {
            new_counter[m.first] = ans;
            ans+= m.second;
        }
        vector<int>result;
        for(int i=0; i<old_nums.size();i++)
        {
            result.push_back(new_counter[old_nums[i]]);
        }
        return result;
    }
};
