#set the initial number to zero
#we will lopp through 1to 11 in order to print the numbers sum
# we will initiate the previous number to iterator
print()
initial_number =0

for i in range(1,11):
    x_sum=initial_number+i
    print("the current number is:",i,"Prious number",initial_number,"sum is:",x_sum)
    initial_number=i