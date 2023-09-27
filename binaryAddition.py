a="1100"
b="0011"
carry=0
print(carry)
arr=[i for i in a]
arr2=[i for i in b]
mini=min(arr,arr2)
maxi=max(arr,arr2)
while(len(mini)!=len(maxi)):
    mini.insert(0,'0')
sum=[]
for i in range(0,len(maxi)):
    if maxi[i]==mini[i]:
        sum.append(0)
    else:
        sum.append(1)
print(sum)    
