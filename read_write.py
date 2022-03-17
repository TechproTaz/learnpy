import os.path

# Check if the file 'raw' exists and returns the value 'True' or 'False'
# then the value gets stored in 'file_exists'
file_exists = os.path.exists('raw') # RAW means Read and Write


if file_exists == True:
    f= open("raw","r")
    if f.mode == 'r':
      contents =f.read()
      print("The contents of the file 'raw' will be shown below")
      print(contents)
      print("Do you want to add another line?(y/n)")
      a = input(">> ")
      if a == "y" or a == "Y":
        print("Please enter your text below")
        x = input(">>")
        f= open("raw","a+")
        f.write("\n" + x)
        f.close() # This will close the instance of the file
        print("Done!")
      else:
        f.close() # This will close the instance of the file
        print("Good bye!")
else:
    f= open("raw","a+")
    print("The file 'raw' has no contents")
    print("Please type something to add it to the file.")
    x = input(">> ")
    f.write(x)
    f.close() # This will close the instance of the file
    print("Done!")
