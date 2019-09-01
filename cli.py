CEND = '\033[0m'
CGREYBG    = '\33[100m'
print(CGREYBG + "Error, does not compute!" + CEND)

def selected_grey(s):
    print(CGREYBG + s + CEND)
