import random
print("")
print("Welcome to the random number game (level 1)")
print("The only way to exscape is to guess the corect number between 1 to 10")
print("")
print("Enter a number between 1 to 10!")
def rangam():
    x = random.randrange(1, 10)
    
    y = int(input(">> "))

    if x == y:
        print("Congrats! That's the correct number!!")
        print("")
    else:
        print("That isn't correct...")
        a = str(x)
        print("The correct number is " + a)
        print("")
        rangam()

rangam()
