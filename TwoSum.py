a=[1,2,6,4]
target=5
def twosum(a,target):
  """
  x+y=target==> y=target-x
                4=5-1 ,4 not in so add {1:0}
                3=5-2 ,3 not in {} so add {1:0,2:1}
               -1=5-6 ,-1 not in {} so add {1:0,2:1,6:2}
                1=5-4 ,  1 found in {1:0,2:1,6:2}
                return current index and index of 1
  """
  buff={}
  for i,num in enumerate(a):
    v=target-num
    if v not in buff:
       buff[num]=i
    else:
      return [i,buff[v]]

res=twosum(a,target)
print(res)
    
###another method                
def twosum(x,t):
    for i in range(len(x)):
        y=t-x[i]
        if y in x:
            index=x.index(y)
            return [i,index]
res=twosum(x,t)
print(res)
