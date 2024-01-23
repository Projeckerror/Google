#!/bin/python
##################################################
#### Author = PANGLIMA JATIM 404              ####
#### Github = https://github.com/Projeckerror ####
####  Time  = Mafia Teknologi                 ####
##################################################
# Jangan di rubah cuk nanti ERROR !
# Jangan Lupa Subscribe chennel YouTube gw

# module
try:
   import os,sys,time,requests,bs4
   from bs4 import BeautifulSoup
   from time import sleep
   from os import system
except:
     system("pip install requests bs4")
# update & upgrade tools
     os.system("pkg update && pkg upgrade")
     os.system("pkg install figlet")
# Module 2
import os
import random
import sys
import time
def mengetik(s):
   for c in s +"\n":
     sys.stdout.write(c)
     sys.stdout.flush()
     time.sleep(random.random()*0.2)
# Animasi 
import os
os.system("clear")
mengetik("\033[1;93mselamat datang di Tools Panglima Jatim 404")
import os
os.system("clear")
mengetik("\033[1;93mJangan Lupa Subcribe Chennel gw ")
import os
os.system("clear")
mengetik("\033[1;93mini adalah sebuah program Google yang di buat oleh Panglima Jatim 404")
import os
os.system("clear")
mengetik("\033[1;93msemoga Program ini bermanfaat untuk kalian semua ok")
import os
os.system("clear")
# Media Sosial
print("\033[36;1m[ Subscribe dulu YouTube gw ]")
time.sleep(1)
os.system("xdg-open https://youtube.com/@PANGLIMAJATIM404")
import os
os.system("clear")
time.sleep(2)
# tampilan
def jalan():
    tampil = """
\033[33;1m           Selamat Datang di Tools Panglima Jatim
\033[1;97m===============================================================
\033[92m Author : Panglima Jatim
\033[1;34m Github : https://github.com/Projeckerror
\033[93m Team   : Mafia Teknologi
\033[1;97m==============================================================="""
    system("clear")
    sleep(1)
    print("\033[36;1m")
    baner = """
   _     _     _     _     _     _    
  / \   / \   / \   / \   / \   / \   
 ( G ) ( o ) ( o ) ( g ) ( l ) ( e )  
  \_/   \_/   \_/   \_/   \_/   \_/  
              \033[38;2;255;165;0m Panglima Jatim 404
  """
    print(baner)
    sleep(1)
    print(tampil)
    # isi data
    file = input("Masukan Pencarian: ")
    ulr = f"https://www.google.com/search?&q={file}"
    r = requests.get(ulr)
    cari = BeautifulSoup(r.text,"html.parser")
    a = cari.find("div",class_="BNeawe").text
    # hasil pencarian
    print("\033[37;1m")    
    print("Hasil \33[36;1m=> ",a)
    # database,waktu,tgl
    import datetime
    now = datetime.datetime.now()
    print("\033[1;97m")
    print(now.strftime("%Y-%m-%d %H:%M:%S"))

jalan()
