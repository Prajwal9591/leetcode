class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        int n = nums.size();
        int left = 0,right = n-1;
        int first = -1,second = -1;
        while(left<=right){
            int mid = left+(right-left)/2;
            if(nums[mid] == target){
                first = mid;
                right = mid-1;
            }
            if(nums[mid] > target){
                right = mid-1;
            }
            if(nums[mid] < target){
                left = mid+1;
            }
        }
        left = 0,right = n-1;
        while(left<=right){
            int mid = left+(right-left)/2;
            if(nums[mid] == target){
                second = mid;
                left = mid+1;
            }
            if(nums[mid] > target){
                right = mid-1;
            }
            if(nums[mid] < target){
                left = mid+1;
            }
        }
        return {first,second};
    }
};