num1=[1,2,4,5,1]
num2=[6,8,9,0,8]
x=[]
y=[]


for i in num1:
    if i%2 == 0:
        x.append(i)

for k in num2:
    if k%2 != 0:
        y.append(k)

        
#merging the list
final=x+y
print(final)