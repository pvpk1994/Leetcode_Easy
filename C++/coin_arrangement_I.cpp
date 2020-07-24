class Solution {
public:
    int arrangeCoins(int n) {
        // n coins are given
        // return complete rows
        int i = 1;
        int n_rows=0;
        if(n<0)
            return -1;
        if(n==1)
            return 1;
        while(n>0)
        {
            if(n>=i)
            {
                n_rows++;
            }
            else{
                break;
            }
            n=n-i;
            i++;
        }
        return n_rows;
    }
};
