class Solution:
    def climbStairs(self, n: int) -> int:

        one=1
        two=1

        for i in range(n-1):

            tmp=one+two
            two=one
            one=tmp
        
        return one