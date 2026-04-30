class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_set<int> seen; 
        for(int i = 0; i < nums.size(); i++)
        {
            if(seen.find(nums.at(i)) != seen.end())
                return true;
            seen.insert(nums.at(i));
        }
        return false;
    }
};