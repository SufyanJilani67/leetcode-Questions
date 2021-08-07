class Solution {
public:
    
    int square(int n){
        int sum = 0;
        while(n){
            int temp = n%10;
            sum += temp * temp;
            n /= 10;
        }
        return sum;
    }
    
    
    bool isHappy(int n) {
        while(square(n) != 1){
            if(n == 89){
                return false;
            }
            n = square(n);
        }
        return true;
        
    }
};