from link_extractor import run_enumeration
from colorama import Fore
from utils.headers import HEADERS
from time import sleep
import requests
import database
import re
import json
from bs4 import BeautifulSoup
import colorama

print(Fore.GREEN + '-----------------------------------' + Fore.RESET, Fore.RED)
print('尸闩㇄尸㠪龱 - Website Link Extractor')
print('     by @RealDebian | V0.02')
print(Fore.GREEN + '-----------------------------------' + Fore.RESET)
print()
sleep(1)

print('Example:')
print()
target_host = str(input('Target Site: '))
print('Select the Protocol (http|https)')
sleep(.5)
protocol = str(input('http=0 | https=1: '))

while True:
    if protocol == '0':
        run_enumeration('http://' + target_host)
        break
    elif protocol == '1':
        run_enumeration('https://' + target_host)
        break
    else:
        print('Wrong option!')

