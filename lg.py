from hashlib import md5
from getpass import getpass
import os
import time


os.system("clear")
index = """\033[1;36m
+____________________________________________+
|__        __   _                          _ |
|\ \      / /__| | ___ ___  _ __ ___   ___| ||
| \ \ /\ / / _ \ |/ __/ _ \| '_ ` _ \ / _ \ ||
|  \ V  V /  __/ | (_| (_) | | | | | |  __/_||
|   \_/\_/ \___|_|\___\___/|_| |_| |_|\___(_)|
+____________________________________________+
[#] Login (#)
"""

print(index)

attempts = 0
check_username = '4a4003cd9ffb5376a2214a04d1fca967'
check_password = '6f708d8a36a332ef10a11e3b474328ae'

while True: 
    print("\n")
    username = input("Username: ")
    password = getpass("Password: ")
    print("\n")

    if attempts == 3:
        print("Too many attempts.")
        exit()

    if md5(username.encode("utf-8")).hexdigest() == check_username:
        if md5(password.encode("utf-8")).hexdigest() == check_password:
            print("[*] Sedang Login...")
            time.sleep(4)
            print("[*] Login Berhasil!")
            time.sleep(1)
            print("[*] Selamat Datang Intruder98")
            time.sleep(2)
            print("[*] Maaf membuat anda menunggu^_^")
            time.sleep(2)
            print("[*] Start your Hack with smile:)")
            time.sleep(2)
            os.system("clear")
            exit()
        else:
        	print("[*] Sedang Login...")
        time.sleep(3)
        print("[*] Dih siapa Lu!! >:(")
        time.sleep(2)
        os.system("killall -9 com.termux")
    else:
        print("Username Salah Goblok")
        time.sleep(2)
        os.system("killall -9 com.termux")
os.system("clear")
