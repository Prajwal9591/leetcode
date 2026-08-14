class Solution {
public:
    int findMaxConsecutiveOnes(vector<int>& nums) {
        int count = 0;
        int max_one = 0;
        for(int i=0; i<nums.size(); i++){
            if(nums[i] == 1){
                count += 1;
            }else{
                count = 0;
            }
            max_one = max(max_one,count);
        }
        return max_one;
    }
};