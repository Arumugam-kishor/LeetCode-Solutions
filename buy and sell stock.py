# prices=[2,2,5]
# profit=0
# left=prices[0]
# right=prices[1]
# while(left!=prices[-1]):
#     if right-left < 0:
#         left=prices[prices.index(right)]
#         if(right==prices[-1]):
#             break
#         else:
#             right=prices[prices.index(right)+1]
#     elif right - left >= profit:
#         profit = right-left
#         if(right==prices[-1]):
#             break
#         else:
#             right=prices[prices.index(right)+1]
#     else:
#         if(right==prices[-1]):
#             break
#         else:
#             right=prices[prices.index(right)+1]
# print(right)
# print(left)
# print(profit)


prices = [2,4,1]
# i=0
# j=len(prices)-1
# profit=0
# while(i<j):
#     profit=max(profit,prices[j]-prices[i])
#     if(prices[i]>prices[j]):
#         i+=1
#     else:
#         j-=1
# print(profit)

# left=0
# right=len(prices)-1
# profit=0
# while left<right:
#     profit=max(profit,prices[right]-prices[left])
#     if prices[left]>prices[right] and prices[-1]!=min(prices):
#         left+=1
#     elif (prices[left]<prices[right]) and max(prices)==prices[-1]:
#         left+=1
#     elif (prices[left]<prices[right]) and min(prices)==prices[-1]:
#         right-=1
#     else:
#         right-=1
# print(profit)


# profit=0
# for i in range(0,len(prices)):
#     for j in range(i+1,len(prices)):
#         if(prices[j]==0):
#             continue
#         if(prices[j]-prices[i]>profit):
#             profit=prices[j]-prices[i]
# print (profit)

prices=[2,1,4]
left=0
right=left+1
profit=0
while right<len(prices)-1:
    if prices[left]<prices[right]:
        profit=max(profit,prices[right]-prices[left])
        right+=1
    else:
        left=right
        right=left+1
print(profit)