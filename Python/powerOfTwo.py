class Solution(object):
    def isPowerOfTwo(self, n):
        import math
        for i in range(0,33):
            if(n==math.pow(2,i)):
                return True
        return False
