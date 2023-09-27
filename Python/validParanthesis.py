class Solution(object):
    def isValid(self, s):
        ascii=[ord(i) for i in s]
        stack=[]
        for i in range(0,len(ascii)):
            stack.append(ascii[i])
            length=len(stack)
            if len(stack)>=2:
                if stack[len(stack)-1]-stack[len(stack)-2]==1 or stack[len(stack)-1]-stack[len(stack)-2]==2:
                    stack.pop(length-1)
                    stack.pop(length-2)
        if len(stack)==0:
            return True
        else:
            return False
