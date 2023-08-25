#### SSH & FTP Brute Forcing Script (Credential Stuffing)
+ This code DOES NOT promote or encourage any illegal activities! The content in this document is 
  provided solely for educational purposes and to create awareness!

#### This is a proof of concept and could be improved on in a lot of ways.
1. To run this code use `git clone https://github.com/`
3. Create Virtual Environment in Windows. Using command `python -m venv sshbruteforcer_env`
4. Run command Linux `source ./sshbruteforcer_env/bin/activate` and Windows `.\sshbruteforcer_env\Scripts\activate`
5. Run the command `pip install -r requirements.txt` to install all the packages required in your virtual environment.
6. Run `python BruteForce.py` this will run the program.


#### Description:
SSH & FTP brute-forcing tool written in python

#### Install
```
▶ git clone https://github.com/hackone103/BruteForce
```

`cd Bruteforce`\
`pip install -r requirements.txt`\
`python BruteForce.py -h`

### Usage : 
```
Show this help message and exit
Usage: python3 BruteForce.py -i [IP] -p [Port] -u [USERNAME] -w [WORDLIST FILE] 
                            -t [THREAD] -T [TIMEOUT] -o [OPTIONS] -oN [OUTPUT]
Basic Help Menu:
     -h,    --help      help           Show this help message and exit
     -i,    --ip        HOSTNAME       Target IP Address
     -p,    --port      PORT           Target Port Number (Default 22)
     -u,    --username  USERNAME       SSH & FTP User name (Default root)
     -w,    --worlist   WORDLIST       Wordlist File Path
     -o,    --option    OPTIONS        Enter Options for SSH & FTP (Default ssh)
     -v,    --verbose   VERBOSE        Enable verbose mode
     -t,    --threads   THREAD         No of threads (Default 9 Exaption ssh maxumum 9 thrades and 
                                       increas outpu error)
     -T,    --timeout   TIMEOUT        Request timeout (Default 5)
     -oN,   --output    OUTPUT         Output file name
```

### Tested on ✅
`Kali Linux`\
`Ubuntu`\
`Termux(Android)`\
`Windows`\
 
### Not Tested on ❌
`Mac OS`\

### Requirements Python

`ftplib`\
`paramiko`\
`threading`\
`queue`\
`sys`\
`socket`\
`time`\
`argparse`\


