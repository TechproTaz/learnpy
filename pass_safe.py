import gc
import os.path
import hashlib
import os
import getpass
import pyautogui
from sys import exit


#def passtype():
#    print("pass in * or invisible? (a/b)")
#    c = input(" >> ")
#    if c == "a" or c == "A":



def new():
#    passtype()
    
    x = input("Enter your name: ")
    # hashed_x = hashlib.sha256(x.encode('utf-8')).hexdigest() # Hashed is sha256
    y = getpass.getpass("Enter your password: ")
    # hashed_y = hashlib.sha256(y.encode('utf-8')).hexdigest() # Hashed is sha256
    
    strings = [x, y]
    hashed_strings = [hashlib.sha256(string.encode('utf-8')).hexdigest() for string in strings]
    '''
    hashed_strings = []
    for string in strings:
        hashed_strings.append(hashlib.sha256(string.encode('utf-8')).hexdigest())
    '''
    hashed_stringss = str(hashed_strings)
    f= open("hash","a+")
    f.write(hashed_stringss)
    print("Your new password is saved!")
    del f

def old():
    f= open("hash","r")
    contents = f.read()
    x = input("Enter your username: ")
    #new_x = hashlib.sha256(x.encode('utf-8')).hexdigest()
    y = getpass.getpass("Enter your password: ")
    #new_y = hashlib.sha256(y.encode('utf-8')).hexdigest()

    strings = [x, y]
    hashed_strings = [hashlib.sha256(string.encode('utf-8')).hexdigest() for string in strings]

    hashed_stringss = str(hashed_strings)

    if hashed_stringss == contents:
        print("The username and password is correct!")
    else:
        print("The username and/or the password is incorrect!")
    del f

'''
from os import walk
f = []
for (dirpath, dirnames, filenames) in walk():
    f.extend(filenames)
    break

print(f)
'''
gc.collect(generation=2)
file_exists = os.path.exists('hash')
if file_exists == True:
    #os.remove("hash")
    old()
else:
    new()

'''
tasks:
1. make users 
pass file e username soho password hashed thaakbe
ar username locate kore porer line password dhore oitar sathe match korbe
username ar password 2 tai hashed thakbe
'''
