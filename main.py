from time import sleep
import random
import os
from math import sqrt
from math import pi
import random
from sys import exit

# The screen clear function
def sclear():
   # for mac and linux(here, os.name is 'posix')
   if os.name == 'posix':
      _ = os.system('clear')
   else:
      # for windows platfrom
      _ = os.system('cls')
# now call function we defined above
sclear()

def calclogo():
    print("""
       ______      __           __      __            
      / ____/___ _/ /______  __/ /___ _/ /_____  _____
     / /   / __ `/ / ___/ / / / / __ `/ __/ __ \/ ___/
    / /___/ /_/ / / /__/ /_/ / / /_/ / /_/ /_/ / /    
    \____/\__,_/_/\___/\__,_/_/\__,_/\__/\____/_/     v1.0
                                                  
    """)
    sleep(0.5)


################################
## The main of calc
def calc():
    sclear()
    calclogo()
    print(" 1. Addition")
    print(" 2. Substraction")
    print(" 3. Multiplication")
    print(" 4. Divition")
    print(" b. Back to main menu")
    print(" q. Quit")
    c = str(input(" >> "))
    if c == "1":
        caladd()
    elif c == "2":
        calsub()
    elif c == "3":
        calmul()
    elif c == "4":
        caldiv()
    elif c == "b" or c == "B":
        mainm()
    elif c == "q" or c == "Q":
        print(" Good bye!")
        exit()
    else:
        print(" calc no")

################################
## 
def caladd():
    sclear()
    calclogo()

    i = 0
    sum = 0
    caladn = 0
    print(" How many numbers do you want to add?")
    while True:
        try:
            caladn = int(input(" >> "))
        except ValueError:
            print(" Not a number!")
            continue
        else:
            while i < caladn:
                print(" Enter a number to add")
                valuee = int(input(" >> "))
                if valuee == '':
                    print(" Please enter a number")
                else:
                    value = int(valuee)
                    sum = sum + value
                    i += 1
            summ = str(sum)
        print(" The summition of those numbers are " + summ)
        print(" Press enter to continue")
        input()
        mainm()

################################
## 
def calsub():
    sclear()
    calclogo()

    print(" Enter first number")
    x = int(input(" >> "))
    print(" Enter second number")
    y = int(input(" >> "))
    if x > y or x == y:
        z = x - y
        zz = str(z)
        print(" " + zz)
        input()
        mainm()
    else:
        print(" The second number is greater than the first number")
        print(" Press enter to continue")
        input()
        calsub()

################################
## 
def calmul():
    sclear()
    calclogo()
    
    print(" Enter first number")
    x = int(input(" >> "))
    print(" Enter second number")
    y = int(input(" >> "))
    print(x * y)
    print(" Press enter to continue")
    input()
    mainm()

################################
## 
def caldiv():
    sclear()
    calclogo()

    print(" Enter first number")
    x = int(input(" >> "))
    print(" Enter second number")
    y = int(input(" >> "))
    print(x / y)
    print(" Press enter to continue")
    input()
    mainm()

################################
## 
def gtn():
    sclear()
    #gtnlogo()
    print("")
    print(" Welcome to the random number game (level 1)")
    print(" The only way to exscape is to guess the corect number between 1 to 10")
    print("")
    print(" Enter a number between 1 to 10!")
    def rangam():
        x = random.randrange(1, 10)
        
        y = int(input(">> "))

        if x == y:
            print("")
            print(" Congrats! That's the correct number!!")
            print(" Press enter to go to menu")
            input()
            mainm()
        else:
            sclear()
            print("")
            print(" That isn't correct...")
            a = str(x)
            print(" The correct number is " + a)
            print("")
            rangam()

    rangam()

def  temp():
    sclear()
    #templogo()
    print(" ------The Temperature Converter------\n")
    print(" Info: Temp scale => C = celcius, F = farenheit and K = Kelvin\n")
    print(" 1. Fahrenheit => Celsius")
    print(" 2. Celsius => Fahrenheit")
    print(" 3. Fahrenheit => Kelvin")
    print(" 4. Celsius => Kelvin")
    print(" 5. Kelvin ==> Celsius")
    print(" 6. Kelvin ==> Fahrenheit")
    print(" q. Quit.")
    print(" x. Go to main menu")
    tempc = input(" >> ")
    # 1. Fahrenheit => Celsius
    if tempc == "1":
        print(" Please enter the temparature in Farenheit")
        tempfa = float(input(" >> "))
        tempce = (5.0 / 9.0) * (tempfa - 32.0)
        tempfas = str(tempfa)
        tempces = str(tempce)
        print(tempfas + "F = " + tempces + "C")
        print(" Press enter to continue")
        input()
        temp()
    # 2. Celsius => Fahrenheit
    elif tempc == "2":
        print(" Please enter the temparature in Celsius")
        tempce = float(input(" >> "))
        tempfa  = (tempce * 9.0 / 5.0) + 32.0
        tempfas = str(tempfa)
        tempces = str(tempce)
        print(tempces + "C = " + tempfas + "F")
        print(" Press enter to continue")
        input()
        temp()
    # 3. Fahrenheit => Kelvin
    elif tempc == "3":
        print(" Please enter the temparature in Fahrenheit")
        tempfa = float(input(" >> "))
        tempke = 273.15 + ((tempfa - 32.0) * (5.0/9.0))
        tempfas = str(tempfa)
        tempkes = str(tempke)
        print(tempfas + "F = " + tempkes + "K")
        print(" Press enter to continue")
        input()
        temp()
    # 4. Celsius => Kelvin
    elif tempc == "4":
        print(" Please enter the temparature in Celsius")
        tempce = float(input(" >> "))
        tempke = tempce + 273.15
        tempces = str(tempce)
        tempkes = str(tempke)
        print(tempces + "C = " + tempkes + "K")
        print(" Press enter to continue")
        input()
        temp()

    # 5. Kelvin ==> Celsius
    elif tempc == "5":
        print(" Please enter the temparature in Kelvin")
        tempke = float(input(" >> "))
        tempce = tempke - 273.15
        tempkes = str(tempke)
        tempces = str(tempce)
        print(tempkes + "K = " + tempces + "C")
        print(" Press enter to continue")
        input()
        temp()
    # 6. Kelvin ==> Fahrenheit
    elif tempc == "6":
        print(" Please enter the temparature in Kelvin")
        tempke = float(input(" >> "))
        tempfa = ((180 * tempke) - 45967) / 100
        tempfas = str(tempfa)
        tempkes = str(tempke)
        print(tempkes + "K = " + tempfas + "F")
        print(" Press enter to continue")
        input()
        temp()
    elif tempc == "q" or tempc == "Q":
        mainm()
    elif tempc == "x" or tempc == "X":
        print(" Good bye!")
        sleep(0.5)
        exit()

def ooe():

    sclear()

    #ooelogo()
    num = int(input("Enter any number to test whether it is odd or even: "))

    if (num % 2) == 0:

        print("The number is even")

    else:

        print("The provided number is odd")

def ac():
    sclear()
    print("----------Area Calculator----------\n")
    print(" 1. Cube \n")#           //borgo
    print(" 2. Circle \n")#         //britto
    print(" 3. Rectangle \n")#      //ayoto
    print(" 4. Triangle\n")#        //trivuj
    print(" 5. Parallelogram\n")#   //samantorik
    print(" q. Quit.\n")
    print(" x. Go to main menu\n")
    print(" Enter your choice (1/2/3/4/5/q/x)")
    aaa = input(" >> ")

    if aaa == '1':

        sclear()
        print(" Enter the side of square: ")
        square_side = input(" >> ")
        # calculation of the area
        area = square_side * square_side
        areas = str(area)

        print(" Area of the square: " + areas)
        print(" Press enter to continue")
        input()
        ac()

    elif aaa == '2':
    
        sclear()
        
        #// take radius as input
        print(" Enter the radius of circle")
        radius = input(" >> ")
        #//Do the Maths!!
        area_circle = pi * radius * radius

        #//Print out le answer
        print(" Area of circle : " +  area_circle)
        print(" Press enter to continue")
        input()
        ac()
    

    elif aaa == '3':
    
        sclear()
        print("\n Enter the Length of Rectangle")
        length = input(" >> ")

        print("\n Enter the Breadth of Rectangle")
        breadth = input(" >> ")

        area = length * breadth
        print("\n Area of Rectangle : " + area)
        print(" Press enter to continue")
        input()
        ac()
    

    elif aaa == '4':
    
        sclear()
        print(" Enter the first side of the triangle ")
        a = int(input(" >> "))
        print(" Enter second side of the triangle ")
        b = int(input(" >> "))
        print(" Enter third side of the triangle")
        c = int(input(" >> "))

        s = (a + b + c)/2 #// Semiperimeter
        ss = sqrt(s)

        areaa = (ss*(ss-a)*(ss-b)*(ss-c))

        print(" Area of the triangle = " + areaa)
        print(" Press enter to continue")
        input()
        ac()

    elif aaa == '5':
        sclear()
        print(" Enter base of the given Parallelogram")
        base = input(" >> ")
        print(" Enter altitude of the given Parallelogram")
        altitude = input(" >> ")
        areae = base * altitude
        print(" Area of Parallelogram is: " + areae)
        print(" Press enter to continue")
        input()
        ac()

    elif aaa == 'x' or aaa == 'X':
        sclear()
        mainm()

    #elif aaa == 'q' or aaa == 'q':
    #    asku()

    else:
        sclear()
        print("\n You have entered a invalid option\n")
        print(" Press enter to continue")
        input()
        ac()

def rngask():
    print("\n\nDo you want another number?(y/n)\n")
    ggg = input(" >> ")

    if ggg == 'y' or ggg == 'Y':
        rng()
    elif ggg == 'n' or ggg == 'N':
        mainm()
    else:
        print("\n You have entered a invalid option\n")
        input()
        rngask()

def rng():
    sclear()
    print(" Enter the lowest number")
    lowera = int(input(" >> "))
    print(" Enter the highest number")
    uppera = int(input(" >> "))
    asd = random.randint  (lowera, uppera)
    asdd = str(asd)
    print("\n The random number is " + asdd)
    #num = (rand() % (upper - lower + 1)) + lower
    #print("%d ", num)
    
    rngask()

################################
## 
def mainm():
    sclear()
    print("""
     ▄▄▄       ██▓     ██▓     ██▓ ███▄    █  ▒█████   ███▄    █ ▓█████ 
    ▒████▄    ▓██▒    ▓██▒    ▓██▒ ██ ▀█   █ ▒██▒  ██▒ ██ ▀█   █ ▓█   ▀ 
    ▒██  ▀█▄  ▒██░    ▒██░    ▒██▒▓██  ▀█ ██▒▒██░  ██▒▓██  ▀█ ██▒▒███   
    ░██▄▄▄▄██ ▒██░    ▒██░    ░██░▓██▒  ▐▌██▒▒██   ██░▓██▒  ▐▌██▒▒▓█  ▄ 
     ▓█   ▓██▒░██████▒░██████▒░██░▒██░   ▓██░░ ████▓▒░▒██░   ▓██░░▒████▒
     ▒▒   ▓▒█░░ ▒░▓  ░░ ▒░▓  ░░▓  ░ ▒░   ▒ ▒ ░ ▒░▒░▒░ ░ ▒░   ▒ ▒ ░░ ▒░ ░
     ▒   ▒▒ ░░ ░ ▒  ░░ ░ ▒  ░ ▒ ░░ ░░   ░ ▒░  ░ ▒ ▒░ ░ ░░   ░ ▒░ ░ ░  ░
     ░   ▒     ░ ░     ░ ░    ▒ ░   ░   ░ ░ ░ ░ ░ ▒     ░   ░ ░    ░   
         ░  ░    ░  ░    ░  ░ ░           ░     ░ ░           ░    ░  ░
    """)
    print("")
    print("                    Welcome to my A.I.O. py project!           ")
    print("                 Made by Tofu <tofu.techzone@gmail.com>        ")
    print("##########################################################################")
    sleep(0.5)
    print(" 1. Simple Calculator") # Done! But needs improvement
    print(" 2. Guess the number") # Done! But needs levels
    print(" 3. Average")
    print(" 4. Odd or Even") # Done! But needs improvement
    print(" 5. Temp converter") # Done! But needs improvement
    print(" 6. Area calculator") # Done! But needs improvement
    print(" 7. Score to grade converter")
    print(" 8. Random number generator")
    print(" 9. About my pc")
    print(" 10. About me")
    print(" u. Update")
    print(" e. Exit")
    m = str(input(" >> "))
    if m == "1":
        calc()
    elif m == "2":
        gtn()
    elif m == "4":
        ooe()
    elif m == "5":
        temp()
    elif m == "6":
        ac()
    elif m == "8":
        rng()
    elif m == "e" or m =="E":
        print(" Good bye!")
        sleep(0.5)
        exit()
    elif m == '':
        print(" Please select an option!")
        sleep(1)
        mainm()
    else:
        print(" Please type a valid option!")
        sleep(1)
        mainm()
mainm()
