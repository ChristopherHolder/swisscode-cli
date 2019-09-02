
import os

CEND = '\033[0m'
CGREYBG = '\33[100m'

# comment test by jp
# Helper methods
def print_grey(s):
    print(CGREYBG + s + CEND)

def flush_stdin():
    if os.name == 'nt': os.system('cls')  
    else: os.system('clear') 
    
def print_color_table():
    """
    prints table of formatted text format options
    usage: print('\x1b[6;33;40m' + '<string>' + '\x1b[0m')
    """
    for style in range(8):
        for fg in range(30,38):
            s1 = ''
            for bg in range(40,48):
                format = ';'.join([str(style), str(fg), str(bg)])
                s1 += '\x1b[%sm %s \x1b[0m' % (format, format)
            print(s1)
        print('\n')

