x=[1,2,3,4,5,6,6]
y=[]

def duplicatelist(x):
 y=[]
 for i in x:
    if i not in y:
       y.append(i)
    else:
       return "Duplicate" 
 return "Not Duplicate"

d=duplicatelist(x)
print(d)
