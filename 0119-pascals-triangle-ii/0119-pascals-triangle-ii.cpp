class Solution {
public:
    vector<int> getRow(int rowIndex) {
        long long  ans = 1;
        vector<int> ansR;
        ansR.push_back(1);
        for(int i = 1; i<=rowIndex; i++){
            ans = ans*((rowIndex+1)-i);
            ans = ans/i;
            ansR.push_back(ans);
        }
        return ansR;
    }
};