from __future__ import absolute_import
import os
import sys 
from io import open

try:
    import turtle
except:
    print u"Turtle module is not installed. Installing..."
    os.system(u"pip install turtle")
    import turtle
try:
    import platform
except:
    print u"Platform module is not installed. Installing..."
    os.system(u"pip install platform")
    import platform
try:
    import psutil
except:
    print u"PSutil module is not installed. Installing..."
    os.system(u"pip install psutil")
    import psutil
try:
    import subprocess
except:
    print u"Subprocess module is not installed. Installing..."
    os.system(u"pip install subprocess")
    import subprocess
#import ascii art module (used in specs command)
try:
    from art import *
except:
    print u"Art module is not installed. Installing..."
    os.system(u"pip install art")
    from art import *
try:
    from termcolor import colored
except:
    print u"Termcolor module is not installed. Installing..."
    os.system(u"pip install termcolor")
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
#    os.system("pip install py-cpuinfo")
#    import cpuinfo as cp

ansicolors = {
    u'red': u'\033[91m',
    u'green': u'\033[92m',
    u'yellow': u'\033[93m',
    u'blue': u'\033[94m',
    u'magenta': u'\033[95m',
    u'cyan': u'\033[96m',
    u'white': u'\033[97m',
    u'end': u'\033[0m'
}


#this is the command line startup code
def command_line_start():
    #cyan
    font = "slant"
    print colored(fig.figlet_format("wowCLI", font=font), "cyan")
    #print light blue text
    print colored(u"Type 'help' for a list of commands.", u'yellow')
    print colored(u"Type 'exit' to exit the command line.", u'yellow')
    print colored(u"Type 'turtle' to enter the graphics mode.", u'yellow')
    print colored(u"Type 'yolo' to print yolo.", u'yellow')
    print colored(u"Type 'clear' to clear the screen.", u'yellow')
    print colored(u"Type 'echo' to echo an input.", u'yellow')
    print colored(u"Type 'specs' to see your computer's specs.", u'yellow')
    print colored(u"Type 'restart' to restart the command line.", u'yellow')
    print colored(u"Type 'cmd' to enter a shell command.", u'yellow')
    print colored(u"Type 'pip' to install a module.", u'yellow')

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
        print u"Exiting the graphics mode..."
        #delete the window
        turtle.bye()
        command_parser()
    print u"Type 'esc' to exit the graphics mode."
    print u"Type 'u' to pen up."
    print u"Type 'd' to pen down."
    print u"Type 'up' to move up."
    print u"Type 'down' to move down."
    print u"Type 'left' to move left."
    print u"Type 'right' to move right."
    print u"Type 'space' to clear the screen."
    turtle.setup(width=0.8, height=0.8, startx=None, starty=None)
    turtle.screensize(canvwidth=500, canvheight=500, bg=u'white')
    turtle.penup()
    turtle.goto(0, 0)
    turtle.pendown()
    turtle.speed(0)
    turtle.color(u'black')
    turtle.pensize(1)
    turtle.shape(u'classic')
    turtle.onkey(clear, u'space')
    turtle.onkey(exit_graphics, u'e')
    turtle.onkey(pen_up, u'u')
    turtle.onkey(pen_down, u'd')
    turtle.onkey(up, u'Up')
    turtle.onkey(down, u'Down')
    turtle.onkey(left, u'Left')
    turtle.onkey(right, u'Right')
    turtle.listen()
    turtle.mainloop()
    command_parser(prompt=prompt)

global prompt
prompt = u"&u &d> "
def command_parser(prompt=None):
    #the real prompt will replace %d with the current working directory and %u with the current user
    realprompt = prompt.replace(u"&d", os.getcwdu()).replace(u"&u", os.getlogin())
    command = raw_input(realprompt)
    command = command.lower()
    args = command.split()
    if command == None or command == u"":
        command_parser(prompt=prompt)
    else:
        try:
            command = args[0]
        except:
            command = u""
    if command == u"help":
        print colored(u"Type 'help' for this list of commands.", u'yellow')
        print colored(u"Type 'exit' to exit the command line.", u'yellow')
        print colored(u"Type 'turtle' to enter the graphics mode.", u'yellow')
        print colored(u"Type 'yolo' to print yolo.", u'yellow')
        print colored(u"Type 'clear' to clear the screen.", u'yellow')
        print colored(u"Type 'echo' to echo an input.", u'yellow')
        print colored(u"Type 'specs' to see your computer's specs.", u'yellow')
        print colored(u"Type 'restart' to restart the command line.", u'yellow')
        print colored(u"Type 'cmd' to run a shell command.", u'yellow')
        print colored(u"Type 'pip' to install a module.", u'yellow')
        print colored(u"Type 'prompt' to change the prompt.", u'yellow')
        command_parser(prompt=prompt)
    elif command == u"exit":
        print u"Exiting the command line..."
        sys.exit()
    elif command == u"turtle":
        print u"Entering the graphics mode..."
        graphics_mode()
    elif command == u"yolo":
        print u"yolo"
        command_parser(prompt=prompt)
    elif command == u"clear":
        print u"Clearing the screen..."
        os.system(u'clear')
        command_parser(prompt=prompt)
    elif command == u"echo":
        try:
            print args[1]
        except IndexError:
            print u"No input given."
        command_parser(prompt=prompt)
    elif command == u"specs":
        #get platform (windows, linux, mac)
        #print ascii art of the computer platform (macOS, Linux, Windows 11/10/8/7/XP)
        tprint(platform.system())
        filedir = os.path.dirname(os.path.abspath(__file__))
        f = open(filedir + u"/"+platform.python_implementation()+u".ans", u"r").read()
        print f
        print u"Operating system: " + platform.system()
        print u"Platform: " + platform.platform()
        print u"Release: " + platform.release()
        ptype = platform.processor() if platform.system()==u"Windows" else os.popen(u"/usr/sbin/sysctl -n machdep.cpu.brand_string").read().strip() if platform.system()==u"Darwin" else os.popen(u"cat /proc/cpuinfo").read().strip()
        print u"Processor: " + ptype
        disk = psutil.disk_usage(u"/")
        print u"Storage: " + str(round(disk.total/1000000000)) + "GB (" + str(round(float(disk.total - disk.free)/disk.total*100, 1)) + "% used)"
        print u"Python version: " + platform.python_version()
        print u"Python release: " + platform.python_implementation()
        command_parser(prompt=prompt)
    elif command == u"restart":
        print u"Restarting..."
        #launch this program again
        os.execl(sys.executable, sys.executable, *sys.argv)
    elif command == u"pip":
        try:
            subprocess.call(u"pip install "+ args[1], shell=True)
        except IndexError:
            print u"No module given."
        command_parser(prompt=prompt)
    elif command == u"prompt":
        try:
            prompt = args[1]
        except IndexError:
            print prompt
        command_parser(prompt=prompt)
    elif command == u"cd":
        try:
            os.chdir(args[1])
        except IndexError:
            print u"No directory given."
        command_parser(prompt=prompt)
    elif command == u"ls" or command == u"dir":
        try:
            dir = os.listdir(os.getcwdu())
            for file in dir:
                if not file.startswith(u"."):
                    print file
        except IndexError:
            print u"No directory given."
        command_parser(prompt=prompt)
    elif command == u"pwd":
        print os.getcwdu()
        command_parser(prompt=prompt)
    elif command == u"cmd":
        fullcommand = u""
        for arg in args[1:]:
            fullcommand += arg + u" "
        try:
            subprocess.call(fullcommand, shell=True)
        except IndexError:
            print u"No command given."
        command_parser(prompt=prompt)
    else:
        print u"Invalid command."
        command_parser(prompt=prompt)


command_line_start()
command_parser(prompt=prompt)