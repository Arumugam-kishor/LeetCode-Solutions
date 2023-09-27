import math
n=33
key=0
for i in range(0,33):
    if(n==math.pow(2,i)):
        key=1
if(key==1):
    print(True)
else:
    print(False)