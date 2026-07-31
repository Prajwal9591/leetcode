class Solution {
public:
    vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
        unordered_set<int> set1;
        unordered_set<int> set2;
        for(int i : nums1){
            set1.insert(i);
        }
        for(int x : nums2){
            if(set1.find(x) != set2.end()){
                set2.insert(x);
            }
        }
        vector<int> ans(set2.begin(), set2.end());
        return ans;
    }
};