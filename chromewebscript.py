import subprocess
import time
import webbrowser
import pyautogui

# script to simulate ctr+cmd+f 
fullScreen = """
tell application "System Events"
    tell application "Google Chrome" to activate
    delay 1
    keystroke "f" using {control down, command down}
end tell
"""

def login():
    subprocess.run(["osascript", "-e", fullScreen]) # Activate full screen

    time.sleep(1)
    pyautogui.moveTo(718, 546)  # Move to correct user 
    time.sleep(1)
    pyautogui.click()
    
    time.sleep(1)
    pyautogui.write('no', interval=0.1) # Search for notion
    pyautogui.press('enter')
    time.sleep(1)

    pyautogui.moveTo(1258, 154)  # Move to correct user 
    time.sleep(1)
    pyautogui.click()

    time.sleep(1)
    pyautogui.moveTo(712, 400)  # Login with google 
    pyautogui.click()

    time.sleep(3)
    pyautogui.moveTo(700, 550)  # Move to correct google account for login  
    time.sleep(1)
    pyautogui.click()  




def main():
    login()

main()