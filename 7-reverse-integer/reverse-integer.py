class Solution:
    def reverse(self, x: int) -> int:
        
        x=str(x)
        x=list(x)
        
        left=0
        right=len(x)-1
        while(left <= right):
            if (x[left]=="+" or x[left]=="-" or x[left]=="*" or x[left]=="/"):
                left+=1
                continue
            elif (x[right]=="+" or x[right]== "-" or x[right]=="*" or x[right]=="/"):
                right-=1
                continue
            else:

                temp=x[left]
                x[left]=x[right]
                x[right]=temp
                left+=1
                right-=1   

        x="".join(x)
        x=int(x)
        if x <-2**31 or x >2**31 -1:
            return 0
        return x
       
             