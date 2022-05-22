#!/usr/bin/env python3

#this will be a small text based OS
#it will have the following features:
#1. a command line
    #commands:
        #echo
        #help
        #exit
        #turtle
        #yolo
        #clear
        #specs
        #cmd
        #restart
        #pip3
#2. a graphics mode (turtle)
#the graphics mode will let you use arrow keys to move the turtle
#keys:
    #up
    #down
    #left
    #right
    #space (clear screen)
    #esc (exit graphics mode)
    #u (pen down)
    #d (pen up)
#the cmd command will allow you to enter a shell command
#if a required module is not installed, it will be installed

#detect if turtle is installed


import os
import sys
try:
    import turtle
except ModuleNotFoundError:
    print("Turtle is not installed. Installing...")
    os.system("pip3 install turtle")
    import turtle
try:
    import platform
except ModuleNotFoundError:
    print("Platform is not installed. Installing...")
    os.system("pip3 install platform")
    import platform
try:
    import psutil
except ModuleNotFoundError:
    print("PSutil is not installed. Installing...")
    os.system("pip3 install psutil")
    import psutil
try:
    import subprocess
except ModuleNotFoundError:
    print("Subprocess is not installed. Installing...")
    os.system("pip3 install subprocess")
    import subprocess
#import ascii art module (used in specs command)
try:
    from art import *
except ModuleNotFoundError:
    print("Art is not installed. Installing...")
    os.system("pip3 install art")
    from art import *
try:
    from termcolor import colored
except ModuleNotFoundError:
    print("Termcolor is not installed. Installing...")
    os.system("pip3 install termcolor")
    from termcolor import colored

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
    #lime green
    print(colored("", 'red'))
    tprint("wowCLI")
    #print light blue text
    print(colored("Type 'help' for a list of commands.", 'yellow'))
    print(colored("Type 'exit' to exit the command line.", 'yellow'))
    print(colored("Type 'turtle' to enter the graphics mode.", 'yellow'))
    print(colored("Type 'yolo' to print yolo.", 'yellow'))
    print(colored("Type 'clear' to clear the screen.", 'yellow'))
    print(colored("Type 'echo' to echo an input.", 'yellow'))
    print(colored("Type 'specs' to see your computer's specs.", 'yellow'))
    print(colored("Type 'restart' to restart the command line.", 'yellow'))
    print(colored("Type 'cmd' to enter a shell command.", 'yellow'))
    print(colored("Type 'pip3' to install a module.", 'yellow'))


def echo():
    print("Type your input.")
    inputtext = input(">> ")
    print(inputtext)
    command_parser()


def graphics_mode():
    def clear():
        turtle.clear()
    def pen_up():
        turtle.penup()
    def pen_down():
        turtle.pendown()
    def up():
        turtle.setheading(90)
        turtle.forward(10)
    def down():
        turtle.setheading(270)
        turtle.forward(10)
    def left():
        turtle.setheading(180)
        turtle.forward(10)
    def right():
        turtle.setheading(0)
        turtle.forward(10)
    def exit_graphics():
        print("Exiting the graphics mode...")
        #delete the window
        turtle.bye()
        command_parser()
    print("Type 'esc' to exit the graphics mode.")
    print("Type 'u' to pen up.")
    print("Type 'd' to pen down.")
    print("Type 'up' to move up.")
    print("Type 'down' to move down.")
    print("Type 'left' to move left.")
    print("Type 'right' to move right.")
    print("Type 'space' to clear the screen.")
    turtle.setup(width=0.8, height=0.8, startx=None, starty=None)
    turtle.screensize(canvwidth=500, canvheight=500, bg='white')
    turtle.penup()
    turtle.goto(0, 0)
    turtle.pendown()
    turtle.speed(0)
    turtle.color('black')
    turtle.pensize(1)
    turtle.shape('classic')
    turtle.onkey(clear, 'space')
    turtle.onkey(exit_graphics, 'e')
    turtle.onkey(pen_up, 'u')
    turtle.onkey(pen_down, 'd')
    turtle.onkey(up, 'Up')
    turtle.onkey(down, 'Down')
    turtle.onkey(left, 'Left')
    turtle.onkey(right, 'Right')
    turtle.listen()
    turtle.mainloop()


def command_parser():
    command = input(">> ")
    command = command.lower()
    if command == "help":
        print(colored("Type 'help' for this list of commands.", 'yellow'))
        print(colored("Type 'exit' to exit the command line.", 'yellow'))
        print(colored("Type 'turtle' to enter the graphics mode.", 'yellow'))
        print(colored("Type 'yolo' to print yolo.", 'yellow'))
        print(colored("Type 'clear' to clear the screen.", 'yellow'))
        print(colored("Type 'echo' to echo an input.", 'yellow'))
        print(colored("Type 'specs' to see your computer's specs.", 'yellow'))
        print(colored("Type 'restart' to restart the command line.", 'yellow'))
        print(colored("Type 'cmd' to enter a shell command.", 'yellow'))
        print(colored("Type 'pip3' to install a module.", 'yellow'))
        command_parser()
    elif command == "exit":
        print("Exiting the command line...")
        sys.exit()
    elif command == "turtle":
        print("Entering the graphics mode...")
        graphics_mode()
    elif command == "yolo":
        print("yolo")
        command_parser()
    elif command == "clear":
        print("Clearing the screen...")
        os.system('clear')
        command_parser()
    elif command == "echo":
        echo()
    elif command == "specs":
        #get platform (windows, linux, mac)
        #print ascii art of the computer platform (macOS, Linux, Windows 11/10/8/7/XP)
        tprint(platform.system())
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
        command_parser()
    elif command == "restart":
        print("Restarting...")
        #launch this program again
        os.execl(sys.executable, sys.executable, *sys.argv)
    elif command == "cmd":
        print("Input a command to execute:")
        cmd = input("$> ")
        #call using subprocess
        subprocess.call(cmd, shell=True)
        command_parser()
    elif command == "pip3":
        print("What module would you like to install?")
        inputthing = input("Module: ")
        subprocess.call("pip3 install "+inputthing, shell=True)
        command_parser()
    elif command == "":
        command_parser()
    else:
        print("Invalid command.")
        command_parser()


command_line_start()
command_parser()