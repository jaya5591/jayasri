def reverseInteger(num):
   res=int(str(num)[::-1]) if num>0 else int('-'+ str(num)[::-1][-1])
   return res

x=reverseInteger(123)
print(x)
