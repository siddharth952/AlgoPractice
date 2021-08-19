class Solution {
public:
    /*
        
    
    */
    bool canPlaceFlowers(vector<int>& flowerbed, int n) {
        int len = flowerbed.size(), cnt = 0;
        vector<int> A(len+2,0);
        // Data preprocess
        for(int i=0;i<len;i++){
            A[i+1] = flowerbed[i];
        }
        
        // Check adjacent for flowers if there are none add
        for(int i=1;i<=len;i++){
            if( A[i-1] == 0 and A[i] == 0 and A[i+1] == 0){
                cnt++;
                A[i] = 1;
            }
        }
        cout << cnt;
        return cnt >= n;
        
    }
};