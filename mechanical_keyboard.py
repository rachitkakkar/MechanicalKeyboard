# Author: Rachit Kakkar
# Last Updated: August 7th, 2022
# Description: Make any keyboard sound like a mechanical one by playing a sound on a keypress!
from playsound import playsound
from pynput.keyboard import Listener
from random import randint

released = True # Keep a variable to determine whether a key has been released
def on_press(key):
    global released
    if (released): # Only play the first time a key has been pressed to avoid repeat sounds when a key is held
        playsound(f'sounds/{randint(1, 5)}.mp3') # Play one of 5 random sounds!
        released = False

def on_release(key): # Set released to true on key release
    global released
    released = True

print('MechanicalKeyboard by Rachit Kakkar has launched!')
print('You should hear sounds now, if on MacOS please accept permissions!')

while True:
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
