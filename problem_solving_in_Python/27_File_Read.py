with open("test.txt","r") as fp:
   lines= fp.readlines()

with open("new_file.txt","w") as fp:
    counter= 0

    for line in lines:

        if counter == 4:
            counter += 1
            continue
        else:

            fp.write(line)

        counter+=1