def divison(numlist):
    print("Given number list is :",numlist)
    x=[]
    for i in numlist:
        if i%5 == 0:
           x.append(i)
        return x


numbers=[60,78,75,90,100]
mylist=divison(numbers)
print(mylist)
