import time
import pyautogui
import subprocess
import platform
import os

# script to simulate ctr+cmd+f 
fullScreen = """
tell application "System Events"
    tell application "Notion" to activate
    delay 1
    keystroke "f" using {control down, command down}
end tell
"""
quit = """
tell application "System Events"
    keystroke "q" using {command down}
end tell
"""

# This function assumes 
# * Static coordinates for buttons 
def login():
    subprocess.run(["open", "/Applications/Notion.app"])

    time.sleep(3)
    pyautogui.moveTo(720, 320)  # Move to on google login button
    pyautogui.click()

    time.sleep(3)
    pyautogui.moveTo(700, 550)  # Move to correct google account for login  
    pyautogui.click()   

    time.sleep(3)
    subprocess.run(["osascript", "-e", fullScreen]) # Activate full screen


def cleanup():
    time.sleep(1)
    subprocess.run(["osascript", "-e", fullScreen]) # Open full screen
    time.sleep(3)
    pyautogui.moveTo(191, 102)
    time.sleep(1)
    pyautogui.click()

    time.sleep(1)
    pyautogui.moveTo(147, 391)
    time.sleep(1)
    pyautogui.click()

    time.sleep(2)
    subprocess.run(["osascript", "-e", quit]) # Open full screen
    # Should write a code to delete the files created

def new_page():
    pyautogui.moveTo(78, 145)  # Move to "new page"-button  


# Assumes macOS
def main():
    login()
    cleanup()




main()