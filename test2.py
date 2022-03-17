from cryptography.fernet import Fernet
import os.path
import hashlib
import os
import getpass
import pyautogui
from sys import exit
from pathlib import Path
def open_file(path_to_file, attempts=0, timeout=5, sleep_int=5):
    if attempts < timeout and os.path.exists(path_to_file) and os.path.isfile(path_to_file): 
        try:
            file = open(path_to_file)
            return file
        except:
            # perform an action
            sleep(sleep_int)
            open_file(path_to_file, attempts + 1)

def main():
    print(" What do you want to do?")
    print(" 1. Encrypt a file")
    print(" 2. Decrypt a file")
    print(" 3. Create a new key")
    inp = input(" >> ")
    if inp == "1":
            print(" Enter the name of your key (case sensitive)")
            nameyy = input(" >> ")
            isitt = nameyy + ".key"
            isit = str(os.path.exists(isitt))
            while isit == "False":
                print(" Dude, that stuff doesn't exist in your current directory")
                print(" Type the name again!!")
                nameyy = input(" >> ")
                isitt = nameyy + ".key"
                isit = str(os.path.exists(isitt))
                
            os.path.exists("nameyy")
            namey = nameyy + ".key"
            #key = return open(nameyy, "rb").read()
            
            #file_exists = os.path.exists(namey) ## COMPLEATE THIS LATER
            keyy = open(namey, "rb")
            key = keyy.read()
            
            print(" Enter the name of the file you want to encrypt \n with file extention (i.e. file.txt)")
            filee = input(" >> ")
            isitt = filee
            
            isit = str(os.path.exists(isitt))
            while isit == "False":
                print(" Dude, that stuff doesn't exist in your current directory")
                print(" Type the name again!!")
                filee = input(" >> ")
                isitt = filee
                isit = str(os.path.exists(isitt))
            
            
            f = Fernet(key)
            with open(filee, 'rb') as original_filee:
                original = original_filee.read()
            encrypted = f.encrypt(original)
            with open("enc_" + filee, 'wb') as encrypted_filee:
                encrypted_filee.write(encrypted)
            print(" DONE !")
            exit()
    elif inp == "2":
        print(" Enter the name of your key (case sensitive)")
        nameyy = input(" >> ")
        
        isitt = nameyy + ".key"
        isit = str(os.path.exists(isitt))
        while isit == "False":
            print(" Dude, that stuff doesn't exist in your current directory")
            print(" Type the name again!!")
            nameyy = input(" >> ")
            isitt = nameyy + ".key"
            isit = str(os.path.exists(isitt))
        
        namey = nameyy + ".key"
        keyy = open(namey, "rb")
        key = keyy.read()
        print(" Enter the name of the file you want to decrypt \n with file extention (i.e. file.txt)")
        den = str(input(" >> "))
        
        isitt = den
        isit = str(os.path.exists(isitt))
        while isit != "True":
            print(" Dude, that stuff doesn't exist in your current directory")
            print(" Type the name again!!")
            den = str(input(" >> "))
            isitt = den
            isit = str(os.path.exists(isitt))
        
        print("")
        f = Fernet(key)
        
        with open(den, "rb") as filee:
        # read the encrypted data
            encrypted_data = filee.read()
        # decrypt data
            decrypted_data = f.decrypt(encrypted_data)
        # write the original file
        with open("dec_" + den, "wb") as filee:
            filee.write(decrypted_data)
        
        '''
        with open(den, 'rb') as encrypted_filee:
            encrypted = encrypted_filee.read()
            
        decrypted = f.decrypt(encrypted)
        
        with open("dec_" + den, 'wb') as decrypted_filee:
            decrypted_filee.write(decrypted)
        '''
        print(" DONE !")
        exit()
        
    elif inp == "3":
        print(" Enter a name for your key")
        myykey = input(" >> ")
        
        isitt = myykey + ".key"
        isit = str(os.path.exists(isitt))
        while isit == "True":
            print(" Dude, there is already a key with the \n same name in your current directory")
            print(" Type the name again!!")
            myykey = input(" >> ")
            isitt = myykey + ".key"
            isit = str(os.path.exists(isitt))
        
        key = Fernet.generate_key()
        with open(myykey + ".key", 'wb') as mykey:
            mykey.write(key)
        print(" DONE !")
        print(" Your key file name is " + myykey + ".key")
        exit()
        
main()
#$
