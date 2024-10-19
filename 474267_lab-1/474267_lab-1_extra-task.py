# доп задание. Анимация


import os
import time

SET_COLOR = "\x1b[48;5;"
END = "\x1b[0m"
CLEAR = "\033[H"

WHITE = 255
BLUE = 20
RED = 1
def draw_line(color):
    line = ''
    print(f"{SET_COLOR}{color}m{line}{END}",end = '')

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def animate_letters(letters, duration=1):
    while True:
        for letter in letters:
            clear_console()
            print(letter)
            time.sleep(duration)

if __name__ == "__main__":
    letters = [ f"{SET_COLOR}{WHITE}m{' К '}{END}", f"{SET_COLOR}{BLUE}m{' О '}{END}", f"{SET_COLOR}{RED}m{' Т '}{END}", ';)' ]

    animate_letters(letters)