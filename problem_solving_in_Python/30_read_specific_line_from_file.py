#here we are printing the 4th line from file
with open("Test.txt","r") as fp:
    lines=fp.readlines()
    print(lines[3])

