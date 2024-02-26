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
    subprocess.run(["open", "/Applications/Google Chrome.app"])
    subprocess.run(["osascript", "-e", fullScreen]) # Activate full screen

    # subprocess.run(["osascript", "-e", fullScreen]) # Activate full screen

    # time.sleep(1)
    # pyautogui.moveTo(710, 340)  # Move to on google login button
    # time.sleep(1)
    # pyautogui.click()

    # time.sleep(3)
    # pyautogui.moveTo(700, 550)  # Move to correct google account for login  
    # time.sleep(1)
    # pyautogui.click()   

    # time.sleep(5)

def main():
    login()

main()