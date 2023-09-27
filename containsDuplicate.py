nums = [1,2,3,4]
nums.sort()
for i in range(0,len(nums)-1):
    if(nums[i]==nums[i+1]):
        print('true')
print('false')
