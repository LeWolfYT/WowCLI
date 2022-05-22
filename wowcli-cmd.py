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

#main loop
print(text2art("WowCLI-CMD")) #print logo
while True:
    #get input
    command = input("$> ")
    if command == "exit":
        print("Goodbye!")
        exit()
        #we need these lines because the command line exit function doesn't work
    elif command == "neofetch":
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
    else:
        os.system(command)