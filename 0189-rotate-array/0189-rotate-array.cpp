class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        int n = nums.size();
        vector<int> rotated(n);
        k= k%n;
        for(int i = 0; i<n; i++){
            if(n !=  0){
                rotated[i] = nums[(i-k+n)%n];
            }            
        }
        for(int x=0; x<n; x++){
            nums[x] = rotated[x];
        }
    }

};