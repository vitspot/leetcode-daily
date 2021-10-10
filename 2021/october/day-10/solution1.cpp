class Solution {
    public:
        int rangeBitwiseAnd(int mleft, int nright) {
            
            int k = 0;
          while(mleft != nright){
             mleft >>= 1;
             nright >>= 1;
             k++;
          }
          return mleft << k;
        }
    };