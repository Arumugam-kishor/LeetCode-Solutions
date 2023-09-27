height = [3,2,4]
left=0
right=1
water=0
sum1=0
while right<len(height):
    while height[left]>height[right]:
        if right==len(height)-1 and left==len(height)-2:
            break        
        elif right==len(height)-1:
            left+=1
            right=left+1
            sum1=0
        else:
            sum1=sum1+(height[left]-height[right])
            right+=1
    water+=sum1
    left=right
    right=left+1
    sum1=0
    if right==len(height)-1 and left==len(height)-2:
            break
print(water)