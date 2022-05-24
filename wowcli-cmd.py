#this is a variation of wowcli
#instead of using built in commands, it uses the default shell
#import modules
import os #we need this for os.system
try:
    import platform #we need this for platform.system()
except:
    print("Platform is not installed. Installing...")
    os.system("pip3 install platform")
    import platform
try:
    import psutil #we need this for psutil.cpu_percent()
except:
    print("PSutil is not installed. Installing...")
    os.system("pip3 install psutil")
    import psutil
try:
    from art import * #we use this to print wowcli logo
except:
    print("Art is not installed. Installing...")
    os.system("pip3 install art")
    from art import *

#make wcsetup.txt if it doesn't exist
try:
    f = open("wcsetup.txt", "r")
    #we run each line of wcsetup.txt as a command
    lines = f.readlines()
    for line in lines:
        os.system("{}".format(line))
    f.close()
except:
    os.system("touch wcsetup.txt")
global prompt
prompt = "*d> "

#main loop
while True:
    #get input
    cwd = os.getcwd()
    nprompt = prompt.replace("*d", cwd)
    nprompt = nprompt.replace("*n", os.getlogin())
    command = input(nprompt)
    if command == "exit":
        print("Goodbye!")
        exit()
        #we need these lines because the command line exit function doesn't work
    elif command == "specfetch":
        print("\033[94m          .?77777777777777$.")
        print("\033[94m          777..777777777777$+           ")
        print("\033[94m         .77    7777777777$$$           ")
        print("\033[94m         .777 .7777777777$$$$           ")
        print("\033[94m         .7777777777777$$$$$$           ")
        print("\033[94m         ..........:77$$$$$$$           ")
        print("\033[94m  .77777777777777777$$$$$$$$$.\033[93m=======.  \033[0m    "+"Operating system: " + platform.system())
        print("\033[94m 777777777777777777$$$$$$$$$$.\033[93m========  \033[0m    "+"Release: " + platform.release())
        print("\033[94m7777777777777777$$$$$$$$$$$$$.\033[93m========= \033[0m    "+"Platform: " + platform.platform())
        print("\033[94m77777777777777$$$$$$$$$$$$$$$.\033[93m========= \033[0m    "+"Processor: " + platform.processor())
        print("\033[94m777777777777$$$$$$$$$$$$$$$$ :\033[93m========+.\033[0m    "+"Machine: " + platform.machine())
        print("\033[94m77777777777$$$$$$$$$$$$$$+..\033[93m=========++~\033[0m    "+"Cores: " + str(psutil.cpu_count())+" cores")
        print("\033[94m777777777$$..\033[93m~=====================+++++\033[0m    "+"Memory: " + str(psutil.virtual_memory().total/1000000000) + " GB")
        print("\033[94m77777777$~.\033[93m~~~~=~=================+++++.\033[0m    "+"Architecture: " + platform.architecture()[0])
        print("\033[94m777777$$$.\033[93m~~~===================+++++++.\033[0m    "+"Storage: " + str(psutil.disk_usage('/').total/1000000000) + " GB")
        print("\033[94m77777$$$$.\033[93m~~==================++++++++: \033[0m    "+"Processes: " + str(len(psutil.pids())))
        print("\033[94m 7$$$$$$$.\033[93m==================++++++++++. \033[0m    "+"Python version: " + platform.python_version())
        print("\033[94m .,$$$$$$.\033[93m================++++++++++~.  \033[0m    "+"Python release: " + platform.python_implementation())
        print("\033[93m         .=========~.........           \033[0m")
        print("\033[93m         .=============++++++           \033[0m")
        print("\033[93m         .===========+++..+++           \033[0m")
        print("\033[93m         .==========+++.  .++           \033[0m")
        print("\033[93m          ,=======++++++,,++,           \033[0m")
        print("\033[93m          ..=====+++++++++=.            \033[0m")
        print("\033[93m                ..~+=... \033[0m")
    elif command == "updatecli":
        print("Updating...")
        #the cli is at https://github.com/LeWolfYT/WowCLI.git
        cwd = os.getcwd()
        os.system("cd ~/")
        #is there a wowcli folder already?
        try:
            os.system("cd ~/WowCLI")
            os.system("git pull")
        except:
            os.system("git clone https://github.com/LeWolfYT/WowCLI.git")
        os.system("cd "+cwd)
    elif command == "clihelp":
        #print help
        print("WOWCLI HELP")
        print("CUSTOM COMMANDS:")
        print("specfetch (alternative to neofetch)")
        print("updatecli (updates the cli, requires git)")
        print("help (this help menu)")
        print("prompt (changes the prompt)")
        print("exit (exits the cli)")
    elif len(command)>7 and command[:6] == "prompt ":
        #change prompt
        #special characters:
        #%*d = cwd
        #%*n = username
        #get what the input is after the word "prompt"
        prompt = command[7:]
    elif command == "prompt":
        print("Current prompt: " + prompt)
    else:
        os.system(command)