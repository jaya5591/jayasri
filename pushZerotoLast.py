a=[2,0,1,3,0,4,0,12]
p=0
for i in range(len(a)):
 if a[i]!=0:
    a[p],a[i]=a[i],a[p]
    p+=1
print(a)
