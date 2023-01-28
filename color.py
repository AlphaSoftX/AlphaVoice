# imports
import os

# enabling colors
os.system("color")

# functions
def write(*values, color=[255, 255, 255], bg=None, sep=None, end=None):
    if type(color) != list:
        raise Exception("Argument 'color' must be type of list!")
    if type(bg) != list and bg != None:
        raise Exception("Argument 'bg' must be type of list!")
    if type(sep) != str and sep != None:
        raise Exception("Argument 'sep' must be type of string!")
    if type(end) != str and end != None:
        raise Exception("Argument 'end' must be type of string!")
    arr = list(map(lambda value: str(value), values))
    if bg == None:
        arr[0] = f"\u001b[38;2;{color[0]};{color[1]};{color[2]}m" + arr[0]
    else:
        arr[0] = f"\u001b[48;2;{bg[0]};{bg[1]};{bg[2]}m\u001b[38;2;{color[0]};{color[1]};{color[2]}m" + arr[0]
    arr[-1] = arr[-1] + "\u001b[0m"
    print(*arr, sep=sep, end=end)

def read(*values, color=[255, 255, 255], bg=None):
    if type(color) != list:
        raise Exception("Argument 'color' must be type of list!")
    if type(bg) != list and bg != None:
        raise Exception("Argument 'bg' must be type of list!")
    string = str(values[0])
    if bg == None:
        string = f"\u001b[38;2;{color[0]};{color[1]};{color[2]}m" + string
    else:
        string = f"\u001b[48;2;{bg[0]};{bg[1]};{bg[2]}m\u001b[38;2;{color[0]};{color[1]};{color[2]}m" + string
    result = input(string)
    print("\u001b[0m", end="")
    return result;