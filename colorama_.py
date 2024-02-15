import termcolor
import pyfiglet
print(pyfiglet.figlet_format((termcolor.colored("Amine", color="red"))))
print(termcolor.colored(pyfiglet.figlet_format("amxnese"), color="cyan"))
print(termcolor.colored("Elzero", color="yellow"))
print(pyfiglet.figlet_format("CR7"))

import colorama
from colorama import Fore, Back, Style
colorama.init()
print(f"{Fore.RED}{Back.GREEN}{Style.BRIGHT} i'm red backgrounded green")