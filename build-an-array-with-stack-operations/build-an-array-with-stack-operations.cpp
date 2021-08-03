class Solution {
public:
    vector<string> buildArray(vector<int>& target, int n) {
        vector<string> ans;  
        int count = 1; 
        int i = 0;
        int size = target.size();
        while (i < size)
        {
            if(count == target [i])
            {
                ans.push_back("Push");
                i += 1;
            }
            else 
            {
                ans.push_back("Push");
                ans.push_back("Pop");
            }
            count += 1;
        }
        return ans;
    }
};