#include <unordered_map>

class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> groups;
        for(string s: strs)
        {
            string sorted_s = s;
            sort(sorted_s.begin(), sorted_s.end());
            groups[sorted_s].push_back(s);
        }

        vector<vector<string>> result;
        for(auto it = groups.begin(); it != groups.end(); ++it)
        {
            result.push_back(it->second);
        }

        return result;
    }
};
