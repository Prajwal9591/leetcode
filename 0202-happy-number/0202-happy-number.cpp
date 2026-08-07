class Solution {
public:
    bool isHappy(int n) {
        unordered_set<int> set;
        
        while(true){
            int ans = 0;
            while(n>0){
                int digit = n % 10;
                ans += digit*digit;
                n = n/10;                
            }
            
            if(ans == 1){
                return true;
            }  
            if(set.find(ans) != set.end()){
                return false;
            }
            set.insert(ans);
            n = ans;
       }
    }
};