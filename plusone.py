digits=[9,9,9,9]
n=len(digits)
digits[n-1]+=1
for i in range (len(digits)-1,0,-1):
    if digits[i]==10:
        digits[i]=0
        digits[i-1]+=1
if(digits[0]==10):
    digits.insert(0,1)
    digits[1]=0
print(digits)