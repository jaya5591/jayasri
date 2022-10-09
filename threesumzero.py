x=[-4,-1,1,2,3,5]

def threesumzero(x):
    out=[]
    for i in range(len(x)-2):
        if i>0 and x[i]==x[i-1]:
            continue
        l=i+1
        r=len(x)-1         
        while l<r:
            target=x[i]+x[l]+x[r]
            if target==0:
                out.append([x[i],x[l],x[r]])
                l+=1
                r-=1
                while l<r and x[l]==x[l-1]:
                    l+=1
                while l<r and x[r]==x[r+1]:
                    r-=1
            elif target>0:
                r-=1
                while l<r and x[r]==x[r+1]:
                    r-=1
            else :
                l+=1
                while l<r and x[l]==x[l-1]:
                    l=l+1
    return out

s=threesumzero(x)
print(s)
