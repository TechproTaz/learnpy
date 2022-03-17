# Substraction Sample

print("Hello, World!")
print("")

x = int(input("x = "))
y = int(input("y = "))

if y < x or x == y:
    print (x - y)
else:
    print("x is smaller then y")
    print("Do u want to substract y reom x? (y/n)")
    z = input(">> ")
    if z == "y":
        print(y - x)
    else:
        print("")
        exit()


print("")

exit()