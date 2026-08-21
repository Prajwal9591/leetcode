class Solution {
public:
    int strStr(string haystack, string needle) {
        int start = 0;
        int i = start;
        int j = 0;
        while(i < haystack.size()){
            if(needle[j] == haystack[i]){
                i++;
                j++;
            }else{
                start++;
                i = start;
                j = 0;
            }
            if(j == needle.size()){
                return start;
            }
            if(start > haystack.size()){
                return -1;
            }
        }
        return -1;
    }
};