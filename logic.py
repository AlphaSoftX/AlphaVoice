# imports
import pyjokes
import wikipedia
import datetime
import time
import subprocess
from functions import takeCommand, username, webbrowser, name, use
from color import write
from colors import green, red, blue, yellow, cyan, pink
from ecapture import ecapture as ec

# main logic function
def runQuery(query):
    global name
    if "hello" in query or query == "hi" or query.startswith("hi "):
        write(f"Hello {use[2]}!", color=green)
    elif "time" in query and "date" in query:
        dt = (datetime.datetime.utcnow() + datetime.timedelta(hours=5, minutes=30))
        write(f"{use[1]}, the date is {dt.strftime('%B %d, %Y (%A)')} and the time is {dt.strftime('%H:%M:%S')}!", color=green)
    elif "date" in query:
        write(f"{use[1]}, the date is {(datetime.datetime.utcnow() + datetime.timedelta(hours=5, minutes=30)).strftime('%B %d, %Y (%A)')}!", color=green)
    elif "time" in query:
        write(f"{use[1]}, the time is {(datetime.datetime.utcnow() + datetime.timedelta(hours=5, minutes=30)).strftime('%H:%M:%S')}!", color=green)
    elif "joke" in query:
        write(f"{use[1]} your joke is:", color=blue)
        time.sleep(.5)
        write(pyjokes.get_joke(), color=green)
        time.sleep(1.5)
        write("Ha Ha Ha!", color=blue)
    elif ("created" in query or "made" in query) and "you" in query:
        write(f"{use[1]}, I was made by Mr. Arun!", color=green)
    elif "who are you" in query:
        write(f"{use[1]}, I am  your Assistant!", color=green)
        time.sleep(.5)
        write("AlphaVoice 1.0", color=blue)
    elif "what are you doing" in query:
        write(f"I am  just following your commands {use[2]}!", color=green)
    elif "stop" in query:
        write("For how much time you want to stop me from taking commands?", color=yellow)
        try:
            ans = int(takeCommand())
            write("AlphaVoice", color=blue, end=" ")
            write("turned off!", color=green)
            time.sleep(ans)
            write("AlphaVoice", color=blue, end=" ")
            write("restarted!", color=green)
        except:
            write("Some error occurred!", color=red)
    elif "who am i" in query or "who i am" in query:
        write(f"I think that you are a human and your name is M{use[0]}. {name}!", color=green)
    elif "reason for you" in query or "why you came to world" in query:
        write("I was created as a Minor project by Mr. Arun, but reason behind my creation is a secret!", color=green)
    elif "you mad" in query or "shut up" in query or "really" in query:
        write("Sorry, did I said something wrong!", color=red)
    elif "how are you" in query:
        write(f"I am fine {use[2]}!", color=green, end=" ")
        write("How are you?", color=yellow)
        ans = takeCommand().lower()
        if "good" in ans or "fine" in ans or "happy" in ans:
            write(f"I am glad to see you fine {use[2]}!", color=green)
        else:
            write("I think you should talk to anyone else about this matter!", color=red)
    elif "love" in query:
        write("It is 7th sense that destroy all other senses!", color=pink)
    elif "change" in query and "name" in query:
        write(f"Now, your name is M{use[0]}. {username()}!", color=green)
    elif "my" in query and "name" in query:
        write(f"{use[1]}, your name is M{use[0]}. {name}!", color=green)
    elif "your" in query and "name" in query:
        write(f"{use[1]}, my name is", color=green, end=" ")
        write("AlphaVoice", color=blue, end="")
        write("!", color=green)
    elif "calculate" in query:
        write("Write your sum", color=cyan, end="")
        ans = takeCommand(": ").lower()
        time.sleep(.5)
        try:
            ans = eval(ans)
            write("Your answer is:", color=green, end=" ")
            write(ans, color=blue)
        except:
            write("Some error occurred!", color=red)
    elif "camera" in query or ("take" in query and "photo" in query):
        ec.capture(0, "AlphaCam", "image.jpg")
    elif "open" in query and "youtube" in query:
        write("Opening YouTube...", color=green)
        webbrowser("youtube.com")
    elif "open" in query and "google" in query:
        write("Opening Google...", color=green)
        webbrowser("google.com")
    elif "open" in query and "website" in query:
        write(f"Which website should I open {use[2]}?", color=yellow)
        ans = takeCommand().lower()
        write("Opening...", color=green)
        webbrowser(ans)
    elif "restart" in query:
        write("This will restart your computer!", color=green)
        time.sleep(.5)
        write("Are you sure? (Y/n)", color=cyan, end="")
        ans = takeCommand(": ").lower()
        if ans == "" or ans == "y" or "yes" in ans:
            time.sleep(.5)
            write("Restarting...", color=green)
            subprocess.call("shutdown /r")
    elif "shut down" in query:
        write("This will shut down your computer!", color=green)
        time.sleep(.5)
        write("Are you sure? (Y/n)", color=cyan, end="")
        ans = takeCommand(": ").lower()
        if ans == "" or ans == "y" or "yes" in ans:
            time.sleep(.5)
            write("Shutting down...", color=green)
            subprocess.call("shutdown /p /f")
    elif "locate" in query:
        write(f"What should I locate {use[2]}?", color=yellow)
        location = takeCommand()
        write(f"Locating {location}...", color=green)
        location = location.replace(" ","+")
        webbrowser("https://www.google.nl/maps/search/"+location)
    elif "wikipedia" in query:
        write(f"What should I search {use[2]}?", color=yellow)
        ans = takeCommand().lower()
        write("Searching Wikipedia...", color=green)
        try:
            results = wikipedia.summary(ans, sentences=3)
            write("According to Wikipedia:", color=blue)
            time.sleep(1)
            write(results, color=green)
        except:
            write("Some error occurred while searching!", color=red)
    elif "write" in query and "note" in query:
        write(f"What should i write, {use[2]}?", color=yellow)
        note = takeCommand().replace("  ", "\n")
        file = open("note.txt", "w")
        write(f"{use[1]}, should I include date and time? (Y/n)", color=cyan, end="")
        sidt = takeCommand(": ")
        if sidt == "" or sidt == "y" or "yes" in sidt:
            dt = (datetime.datetime.utcnow() + datetime.timedelta(hours=5, minutes=30)).strftime("%B %d, %Y (%A) %H:%M:%S")
            file.write(dt)
            file.write("\n")
            file.write(note)
        else:
            file.write(note)
        file.close()
    elif "show" in query and "note" in query:
        write("Showing Note...", color=green)
        try:
            file = open("note.txt", "r")
            write(file.read(), color=blue)
            file.close()
        except:
            write("No note found, please use 'write note' command!", color=red)
    else:
        write(f"{use[1]}, I think you should talk to anyone else about this matter!", color=red)
        time.sleep(.5)
        write("Do you want me to search your query on google! (Y/n)", color=cyan, end="")
        ans = takeCommand(": ").lower()
        if ans == "" or ans == "y" or "yes" in ans:
            time.sleep(.5)
            write("Searching...", color=green)
            webbrowser("google.com/search?q="+query.replace(" ","+"))
            write("Successfully searched!", color=blue)
