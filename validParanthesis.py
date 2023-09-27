s="([)]"
arr=[]
stack=[]
top=0
for i in s:
    arr.append(ord(i))
for i in arr:
    if(i==40 or i==91 or i==123):
        stack.append(i)
        top+=1
    if(i==41):
        arr1=arr[0:arr.index(i)]
        for j in arr1:
            if(j==40):
                stack.remove(40)
                top-=1
    if(i==93):
        arr2=arr[0:arr.index(i)]
        for j in arr2:
            if(j==91):
                stack.remove(91)
                top-=1
    if(i==125):
        arr3=arr[0:arr.index(i)]
        for j in arr3:
            if(j==123):
                stack.remove(123)
                top-=1
if(top==0):
    print('true')
else:
    print('false')