class Solution {
    public:
        int climbStairs(int n) {
         // for n=2 -> 2
        // for n= 3 -> 3
            // for n =4 -> 5
            // for n=5 ->8
            // as we cab see it's forming fibonacci series: sum of previous 2 digits
            int a =1, b=1,c = a+b, i=2;
            if(n == 1) return 1;
            //while conditon will give output starting from n =2;
            while(i++<n){
                a = b;
                b =c;
                c =a+b;
                
            }
            return c;
            
        }
    };