import sys
from colorama import Fore, Back, Style
from termcolor import colored 

colors={'green','yellow','red','blue'}

for i in colors:
    color ="Fore."+i.upper()
    print(colored(Fore.RED,i)) 
