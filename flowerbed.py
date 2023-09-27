class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        flowerbed.insert(0,0)
        flowerbed.append(0)
        i=1
        while True:
            if(n==0):
                return True
            if(i>len(flowerbed)-2):
                return False 
            if(flowerbed[i]==0 and flowerbed[i+1]==0 and flowerbed[i-1]==0):
                n-=1
                i+=2
            else:
                i+=1                   
