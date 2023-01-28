# imports
import warnings
import time
from sys import exit
from color import write
from functions import clear, wishMe, username, takeCommand, use
from logic import runQuery
from colors import green, yellow

# disabling unnecessary warnings
warnings.filterwarnings("ignore")

# global variables
upc = None

# clearing window
clear()

# wishing the user
wishMe()
write(f"\nWelcome M{use[0]}. {username()}", color=green)
time.sleep(1)
write(f"How can I help you {use[2]}?\n", color=yellow)

# starting program
while True:
    query = takeCommand().lower()
    time.sleep(.75)
    if "exit" in query or "bye" in query:
        write(f"Thanks for giving me your precious time {use[2]}, have a nice day!", color=green)
        break
    elif "repeat" in query or (("upper" in query or "last" in query) and "command" in query):
        if upc == None:
            print('No last command found!')
        else:
            runQuery(upc)
    else:
        runQuery(query)
        upc = query
    print()
    time.sleep(1)

# turning off program
time.sleep(.5)
exit()
