def addition(a):
   if a:
       return a+addition(a-1)
   else:
       return 0

result=addition(50)
print(result)


