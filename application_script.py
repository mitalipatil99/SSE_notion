import time
import pyautogui
import subprocess
import platform
import os

fullScreen = """
tell application "System Events"
    tell application "Notion" to activate
    delay 1
    keystroke "f" using {control down, command down}
end tell
"""


# This function assumes 
# * Static coordinates for buttons 
def login(os_name):
    # Opening application
    # Dependent on OS
    # 'posix' for Linux and macOS, 'nt' for Windows
    if os_name == 'nt':
        print("You're using Windows.")
        notion_path = "C:\\Users\\Mitali\\Downloads\\Notion Setup 2.0.47.exe" # notion path change 
        subprocess.Popen(notion_path)
    else:
        print("You're likely using Linux or macOS.")
        subprocess.run(["open", "/Applications/Notion.app"])

    time.sleep(3)
    pyautogui.moveTo(720, 320)  # Move to on google login button
    pyautogui.click()

    time.sleep(3)
    pyautogui.moveTo(700, 550)  # Move to correct google account  
    pyautogui.click()   
    
    time.sleep(3)
    subprocess.run(["osascript", "-e", fullScreen]) # Open full screen




def main():
    os_name = platform.system()
    login(os_name)



main()