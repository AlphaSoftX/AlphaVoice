# imports
import datetime
import time
import os
from color import write, read
from colors import red, green, blue, yellow, cyan

# global variables
name = ""
gender = "f"
obj = {
    "m": ["r", "Sir", "sir"],
    "f": ["rs", "Mam", "mam"]
}
use = obj[gender]

# functions for the program


def takeCommand(sign=None):
    try:
        if sign == None:
            sign = "> "
        return read(sign, color=cyan)
    except:
        write("Sorry, could you repeat that?", color=red)
        return takeCommand()


def username():
    global name
    write(f"What should I call you {use[2]}?", color=yellow)
    name = takeCommand()
    return name


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        write(f"Good Morning {use[1]}!", color=green)
    elif hour >= 12 and hour < 16:
        write(f"Good Afternoon {use[1]}!", color=green)
    else:
        write(f"Good Evening {use[1]}!", color=green)
    time.sleep(1)
    write("I am your Assistant.", color=blue)
    write("AlphaVoice 1.0\n", color=blue)
    time.sleep(1.5)


def clear(): return os.system("cls")

def webbrowser(url):
    os.system("start chrome "+url)