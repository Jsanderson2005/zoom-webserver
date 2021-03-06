import  datetime, time, subprocess, csv, os, webbrowser
import keyboard
import image

def linkjoin(link):
    webbrowser.open(link)
    start = time.time()
    time.sleep(3)
    return

def mute():
    keyboard.press_and_release('cmd+shift+a')

def video():
    keyboard.press_and_release('cmd+shift+v')

def view():
    keyboard.press_and_release('cmd+shift+w')

def fullscreen():
    keyboard.press_and_release('cmd+shift+f')

def meetingChat():
    keyboard.press_and_release('cmd+shift+h')

def end():
    keyboard.press_and_release('cmd+w')
    os.system('pkill -f firefox')
    time.sleep(3)
    os.system('pkill -f zoom.us')

