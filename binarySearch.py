nums = [-1,0,3,5,9,12]
st=0
end=len(nums)
target=int(input("Enter target"))
while(mid!=0):
    mid=(st+end)/2
    if(nums[mid]==target):
        print(nums.index(mid))
    elif(target>mid):
        mid=