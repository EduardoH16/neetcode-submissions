class Solution {
public:

    string encode(vector<string>& strs) {
        string encoded = "";
        for(string s : strs)
        {
            encoded += to_string(s.size()) + "#" + s;
        }
        return encoded;
    }

    vector<string> decode(string s) {
        vector<string> decoded;
        int i = 0;
        while(i < s.size())
        {
            int j = i;
            while(s[j] != '#')
            {
                j++;
            }

            int length = stoi(s.substr(i, j - i));
            
             // Move pointer i to the start of the actual string content
            i = j + 1;
            
            // Extract the string and add to result
            decoded.push_back(s.substr(i, length));
            
            // Move pointer i past the extracted string
            i += length;
        }
        return decoded;
    }
};
