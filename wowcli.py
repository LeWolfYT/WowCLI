import os
import sys

try:
    import platform
except:
    print("Platform module is not installed. Installing...")
    os.system("pip3 install platform")
    import platform
try:
    import psutil
except:
    print("PSutil module is not installed. Installing...")
    os.system("pip3 install psutil")
    import psutil
try:
    import subprocess
except:
    print("Subprocess module is not installed. Installing...")
    os.system("pip3 install subprocess")
    import subprocess
#import ascii art module (used in specs command)
try:
    from art import *
except:
    print("Art module is not installed. Installing...")
    os.system("pip3 install art")
    from art import *
try:
    from termcolor import colored
except:
    print("Termcolor module is not installed. Installing...")
    os.system("pip3 install termcolor")
    from termcolor import colored
try:
    import pyfiglet as fig
except:
    print("pyfiglet module is not installed. Installing...")
    os.system("pip3 install pyfiglet")
    import pyfiglet as fig
#try:
#    import cpuinfo as cp
#except:
#    print("Py-cpuinfo module is not installed. Installing...")
#    os.system("pip3 install py-cpuinfo")
#    import cpuinfo as cp

ansicolors = {
    'red': '\033[91m',
    'green': '\033[92m',
    'yellow': '\033[93m',
    'blue': '\033[94m',
    'magenta': '\033[95m',
    'cyan': '\033[96m',
    'white': '\033[97m',
    'end': '\033[0m'
}


#this is the command line startup code
def command_line_start():
    #cyan
    font = "slant"
    print(colored(fig.figlet_format("wowCLI", font=font), "cyan"))
    #print light blue text
    print(colored("Type 'help' for a list of commands.", 'yellow'))

global prompt
prompt = "&u &d> "
def command_parser(prompt=None):
    #the real prompt will replace %d with the current working directory and %u with the current user
    realprompt = prompt.replace("&d", os.getcwd()).replace("&u", os.getlogin())
    command = input(realprompt)
    command = command.lower()
    args = command.split()
    if command == None or command == "":
        command_parser(prompt=prompt)
    else:
        try:
            command = args[0]
        except:
            command = ""
    if command == "help":
        print(colored("Type 'help' for this list of commands.", 'yellow'))
        print(colored("Type 'exit' to exit the command line.", 'yellow'))
        print(colored("Type 'yolo' to print yolo.", 'yellow'))
        print(colored("Type 'clear' to clear the screen.", 'yellow'))
        print(colored("Type 'echo' to echo an input.", 'yellow'))
        print(colored("Type 'specs' to see your computer's specs.", 'yellow'))
        print(colored("Type 'restart' to restart the command line.", 'yellow'))
        print(colored("Type 'cmd' to run a shell command.", 'yellow'))
        print(colored("Type 'pip3' to install a module.", 'yellow'))
        print(colored("Type 'prompt' to change the prompt.", 'yellow'))
        command_parser(prompt=prompt)
    elif command == "exit":
        print("Exiting the command line...")
        sys.exit()
    elif command == "turtle":
        print("Entering the graphics mode...")
        graphics_mode()
    elif command == "yolo":
        print("yolo")
        command_parser(prompt=prompt)
    elif command == "clear":
        print("Clearing the screen...")
        os.system('clear')
        command_parser(prompt=prompt)
    elif command == "echo":
        try:
            print(args[1])
        except IndexError:
            print("No input given.")
        command_parser(prompt=prompt)
    elif command == "specs":
        #get platform (windows, linux, mac)
        #print ascii art of the computer platform (macOS, Linux, Windows 11/10/8/7/XP)
        tprint(platform.system())
        filedir = os.path.dirname(os.path.abspath(__file__))
        f = open(filedir + "/"+platform.python_implementation()+".ans", "r").read()
        print(f)
        
        print("Operating system: " + platform.system())
        print("Platform: " + platform.platform())
        print("Release: " + platform.release())
        ptype = platform.processor() if platform.system()=="Windows" else os.popen("/usr/sbin/sysctl -n machdep.cpu.brand_string").read().strip() if platform.system()=="Darwin" else os.popen("cat /proc/cpuinfo").read().strip()
        print(f"Processor: {ptype}")
        disk = psutil.disk_usage("/")
        print(f"Storage: {str(round(disk.total/1000000000))} GB ({round(disk.used/disk.total*100, 1)}% used)")
        print("Python version: " + platform.python_version())
        print("Python release: " + platform.python_implementation())
        command_parser(prompt=prompt)
    elif command == "restart":
        print("Restarting...")
        #launch this program again
        os.execl(sys.executable, sys.executable, *sys.argv)
    elif command == "pip3":
        try:
            subprocess.call("pip3 install "+ args[1], shell=True)
        except IndexError:
            print("No module given.")
        command_parser(prompt=prompt)
    elif command == "prompt":
        try:
            prompt = args[1]
        except IndexError:
            print(prompt)
        command_parser(prompt=prompt)
    elif command == "cd":
        try:
            os.chdir(args[1])
        except IndexError:
            print("No directory given.")
        command_parser(prompt=prompt)
    elif command == "ls" or command == "dir":
        try:
            dir = os.listdir(os.getcwd())
            for file in dir:
                if not file.startswith("."):
                    print(file)
        except IndexError:
            print("No directory given.")
        command_parser(prompt=prompt)
    elif command == "pwd":
        print(os.getcwd())
        command_parser(prompt=prompt)
    elif command == "cmd":
        fullcommand = ""
        for arg in args[1:]:
            fullcommand += arg + " "
        try:
            subprocess.call(fullcommand, shell=True)
        except IndexError:
            print("No command given.")
        command_parser(prompt=prompt)
    else:
        print("Invalid command.")
        command_parser(prompt=prompt)


command_line_start()
command_parser(prompt=prompt)