nums = [1,12,-5,-6,50,3]
k = 4
i=0
j=i+k-1
add=0
while(j!=len(nums)):
    newsum=0
    list=nums[i:j+1]
    for l in list:
        newsum=newsum+l 
    add=max(add,newsum)
    i+=1
    j+=1
print(add/k)