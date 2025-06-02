import os
size=os.stat("testing.txt").st_size
if size == 0:
    print("file is empty")
else:
    print("Has some content")
