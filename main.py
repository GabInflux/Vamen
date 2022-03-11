import warnings
import pywhatkit as kt
from pystyle import Colorate, Colors, Center
from os import system
from time import sleep

system('cls')
warnings.filterwarnings("ignore")

boucle1 = True

header = """
 ▄█    █▄     ▄████████   ▄▄▄▄███▄▄▄▄      ▄████████ ███▄▄▄▄   
███    ███   ███    ███ ▄██▀▀▀███▀▀▀██▄   ███    ███ ███▀▀▀██▄ 
███    ███   ███    ███ ███   ███   ███   ███    █▀  ███   ███ 
███    ███   ███    ███ ███   ███   ███  ▄███▄▄▄     ███   ███ 
███    ███ ▀███████████ ███   ███   ███ ▀▀███▀▀▀     ███   ███ 
███    ███   ███    ███ ███   ███   ███   ███    █▄  ███   ███ 
███    ███   ███    ███ ███   ███   ███   ███    ███ ███   ███ 
 ▀██████▀    ███    █▀   ▀█   ███   █▀    ██████████  ▀█   █▀  
 
            V 1.0 - Gab_#8440 - discord.gg/BtNrFc45B7\n\n\n\n"""


while boucle1:
    print(Colorate.Diagonal(Colors.white_to_blue, Center.XCenter(header)))
    print(Colorate.Horizontal(Colors.white_to_blue, "[?] Path of the file ↓"))
    source_path = input("")
    system('cls')

    print(Colorate.Diagonal(Colors.white_to_blue, Center.XCenter(header)))
    print(Colorate.Horizontal(Colors.white_to_blue, "[?] Name of the new file ↓"))
    target_path = input("")
    system('cls')
    
    try:
        kt.image_to_ascii_art(source_path, target_path)
        print(Colorate.Diagonal(Colors.white_to_blue, Center.XCenter(header)))
        print(Colorate.Horizontal(Colors.white_to_blue, f"[!] Succesful creation of ascii image Look at {target_path}.txt !"))
        sleep(5)
        system('cls')
    except:
        print(Colorate.Diagonal(Colors.white_to_blue, Center.XCenter(header)))
        print(Colorate.Horizontal(Colors.white_to_blue, "[!] Error in creation of your ascii image !"))
        sleep(3)
        system('cls')