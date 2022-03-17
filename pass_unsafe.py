# The whole stuff is here
# This is a test login part
# and it is compleately insecure

import time
import base64

'''
print(base64.b64encode("786003134".encode("utf-8")))
print("")
print(base64.b64encode("Nzg2MDAzMTM0".encode("utf-8")))
print("")
print(base64.b64encode("TnpnMk1EQXpNVE0w".encode("utf-8")))
print("")
print(base64.b64encode("VG5wbk1rMUVRWHBOVkUwdw==".encode("utf-8")))
print("")

'''

passa = (base64.b64decode("Vkc1d2JrMXJNVVZSV0hCT1ZrVXdkdz09").decode("utf-8"))
passb = (base64.b64decode(passa).decode("utf-8"))
passc = (base64.b64decode(passb).decode("utf-8"))
passx = (base64.b64decode(passc).decode("utf-8"))


print(" Welcome to the project AIO_0.8")

time.sleep(1)
passc = input(" Enter your password: ")
if passc == passx:
    print(" Welcome!")
else:
    print(" Wrong password!")