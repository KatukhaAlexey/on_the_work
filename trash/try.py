#import keyboard
# 
# def check_state():
#     print("Для продолжения нажмите Enter...")
#     if keyboard.is_pressed('Enter'):
#         print('нажатие')
#     else:
#         print("timeout")
# 
# check_state()
#while keyboard.read_key() == "a" or keyboard.read_key() == "s" or keyboard.read_key() == "d" or keyboard.read_key() == "w":
#    print("You pressed ", keyboard.read_key())
#    #
#
#while True:
#    if keyboard.is_pressed("q"):
#        print("You pressed q")
#        break
#        
#keyboard.on_press_key("r", lambda _:print("You pressed r"))

from pynput import keyboard

def on_press(key):
    try:
        print('Alphanumeric key pressed: {0} '.format(key.char))
    except AttributeError:
        print('special key pressed: {0}'.format(key))

def on_release(key):
    print('Key released: {0}'.format(key))
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Collect events until released
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
