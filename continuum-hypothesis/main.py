import time
from os         import system
from random     import randint
from pynput     import keyboard
from datetime   import datetime

# Constants
N = 10
LETTERS = ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'ñ']

# Variables
i = 0
num = 0
time = 0
listening = True

# Open data file
f = open('data.txt', 'a')

# Set pair of indexes
bti = randint(0, len(LETTERS) - 1)
sti = len(LETTERS) - bti - 1

# Set pair of letters
bt = LETTERS[bti]
st = LETTERS[sti]

# Random number generator
def get_num():
    num = randint(1, 127)
    return num + 1 if num >= 64 else num

# Next number loader
def load_next():
    global i, num
    system('clear')
    num = get_num()
    print(num)
    i += 1

# On keyboard press event listener
def on_press(key):
    global time
    pressed = str(key)[1]

    if i < N:
        if pressed == bt:
            t = datetime.now() - time
            f.write(f'{num} > 64 = {num > 64}, {t}\n')
            load_next()
            time = datetime.now()
        elif pressed == st:
            t = datetime.now() - time
            f.write(f'{num} < 64 = {num < 64}, {t}\n')
            load_next()
            time = datetime.now()
        elif key == keyboard.Key.esc:
            return False
    else:
        return False

# Welcome
system('clear')
print('¡Bienvenido al experimento!')

# Personal data
name = input('Antes que nada, ¿cómo te llamás? ')
age = input(f'¿Cúantos años tenés, {name}? ')
f.write(f'{name} {age}\n')
system('clear')

# Record pair of letters
f.write(f'> = "{bt}", < = "{st}"\n')

# Description
input((
    f'Te explicamos cómo es el desafío: '
    f'te vamos a ir mostrando distintos números '
    f'y vos vas a tener que apretar la tecla '
    f'"{bt}" cuando el número es mayor que 64 '
    f'y "{st}" cuando el número es menor que 64. '
    f'Mientras más rápido lo hagas, mejor. '
    f'Cuando estés liste apretá enter y arrancamos.'
))

# Clear screen before starting
system('clear')

# Define and display num
num = get_num()
print(num)
time = datetime.now()

# Create keyboard listener and init it
with keyboard.Listener(on_press=on_press, suppress=True) as listener:
    listener.join()

# Bye bye
system('clear')
input('¡Gracias!\n')
f.write('\n')
f.close()
