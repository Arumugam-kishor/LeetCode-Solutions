class Solution(object):
    def plusOne(self, digits):
        newf=[]
        c=0
        for i in digits:
            c=c*10+i
        c=c+1
        print(c)
        while(c!=0):
            d=c%10
            c=c//10
            newf.append(d)
        newf.reverse()
        return newf        
