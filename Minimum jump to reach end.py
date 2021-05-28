#Minimum Jump to Reach End

def jump(a,n):
    if n<=1:
        return 0
    
    if a[0]==0:
        return -1
    
    
    maxr=a[0]
    step=a[0]
    
    jump=1
    
    for i in range(1,n):
        maxr=max(maxr,i+a[i])
        if (i==n-1):
            return jump
        
        step-=1
        
        if step==0:
            jump+=1
            
            if i>=maxr:
                return -1
            
            step=maxr-i
    return -1
        
a=[1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
n=len(a)
jump(a,n)