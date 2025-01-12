import keyboard
import sys, subprocess
import shutil
import time
# Wszystko powyżej to powinny być importy.
slow_cd = 0.1 # Zmienna definiująca ile czasu mija w funkcji slowprint() przed wydrukowaniem następnej litery

# Predefiniowane zmienne powyżej
def print_center(text):
    print(text.center(shutil.get_terminal_size().columns))

def slowprint(text):
    for char in text:
        print(char, end = "", flush = True)
        time.sleep(slow_cd)
# powolne drukowanie tekstu
# Wszystko powyżej to powinny być funkcje
keyboard.press('f11') # wchodzisz w tryb fullscreen
time.sleep(1)
IsMenuOn = True
print_center('=======================================================================================')
print_center('             ___               __     __      __   __   __  ___  __   __   __       ')
print_center(' /\  |    | |__  |\ |    \  / /  \ | |  \    |__) |__) /  \  |  /  \ /  ` /  \ |    ')
print_center('/--\ |___ | |___ | \|     \/  \__/ | |__/    |    |  \ \__/  |  \__/ \__, \__/ |___')
print_center('')
print_center('=======================================================================================')
print('')
print('')
print('')
print('')
print('')
print('')
print('')
print_center('[0] Campaign (coming soon!)')
print_center('[1] Gamemodes')
print_center('[2] Quit')
while IsMenuOn == True:
    if keyboard.is_pressed('2'):
        sys.exit()
    elif keyboard.is_pressed('1'):
        pass
    else:
        continue


