with open("D:\Py for AI and DS\Example1.txt","w") as File1:
    File1.write("This is a new Line")
    File1.close()


    with open("D:\Py for AI and DS\Example1.txt","r") as ReadFile:
     ReadFile.read()
     ReadFile.close()   