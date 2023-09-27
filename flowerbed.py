flowerbed=[1,0,0,0,0,1]
n=2
flowerbed.insert(0,0)
flowerbed.append(0)
i=1
while True:
    if(n==0):
        print("True")
        break
    if(i>len(flowerbed)-2):
        print("False")
        break
    if(flowerbed[i]==0 and flowerbed[i+1]==0 and flowerbed[i-1]==0):
        n-=1
        i+=2
    else:
        i+=1    