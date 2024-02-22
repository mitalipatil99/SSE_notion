import time
import pyautogui
import subprocess
import platform
import os

import pyperclip

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
    subprocess.run(["osascript", "-e", fullScreen]) # Activate full screen

    time.sleep(1)
    pyautogui.moveTo(710, 340)  # Move to on google login button
    time.sleep(1)
    pyautogui.click()

    time.sleep(3)
    pyautogui.moveTo(700, 550)  # Move to correct google account for login  
    time.sleep(1)
    pyautogui.click()   

    time.sleep(5)

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
    # Create new page
    time.sleep(3)
    pyautogui.keyDown('command')            # cmd+n = new page
    pyautogui.write('n', interval=0.1)
    pyautogui.keyUp('command')
    time.sleep(1)

    pyautogui.moveTo(366, 517)  # Move to "templates"-button  
    time.sleep(1)
    pyautogui.click()
    time.sleep(1)

    pyautogui.moveTo(188, 120)  # Move to searchbar
    time.sleep(1)
    pyautogui.click()
    time.sleep(1)

    pyautogui.write('notes', interval=0.1)
    time.sleep(1)

    pyautogui.moveTo(212, 215)  # Move to "Cornell"-button  
    time.sleep(1)
    pyautogui.click()
    time.sleep(1)

    pyautogui.moveTo(1170, 670)  # Move to get template
    pyautogui.click()
    time.sleep(1)

def create_page():
    time.sleep(3)
    # Delete the explanation 
    pyautogui.scroll(-100)
    time.sleep(1)
    pyautogui.moveTo(365, 123)  # Move to "Cornell notes system"-header 
    time.sleep(0.1)
    pyautogui.mouseDown()
    time.sleep(1)
    pyautogui.moveTo(1380, 153)  # Move to "Cornell notes system"-header 
    time.sleep(1)
    pyautogui.scroll(100)
    time.sleep(1)
    pyautogui.mouseUp()
    time.sleep(1)
    pyautogui.press('backspace')
    pyautogui.moveTo(365, 123)  # Move to "Cornell notes system"-header 
    pyautogui.mouseDown()

    # Get the class notes template 
    pyautogui.moveTo(954, 365)  # Move to "Cornell notes system"-header 
    time.sleep(1)
    pyautogui.click()
    time.sleep(1)
    # Write heading
    for i in range(20):
        pyautogui.press('backspace')
    time.sleep(1)
    pyautogui.write("CS4415 - Sustainable Software Engineering", interval=0.1)
    time.sleep(2)
    pyautogui.scroll(-100)
    time.sleep(1)
    pyautogui.moveTo(750, 240)  # Move to "Date"-header 
    pyautogui.click()
    time.sleep(1)
    pyautogui.press('backspace')
    time.sleep(0.1) 
    pyautogui.write("@t", interval=0.1)
    time.sleep(0.1) 
    pyautogui.press('enter') 
    pyautogui.moveTo(518, 306)  # Move to "Topic"-header 
    time.sleep(1)
    pyautogui.click()
    time.sleep(0.5)
    pyautogui.write('Green Fintech', 0.1)
    
    time.sleep(1) 
    pyautogui.moveTo(785, 470)  # Move to bullet points
    time.sleep(1)
    pyautogui.click()
    time.sleep(1)
    for i in range(8):
        pyautogui.press('backspace')
    time.sleep(1)
    pyautogui.write('Some cool notes', 0.1)
    time.sleep(0.1) 
    pyautogui.press('enter') 
    pyautogui.write('Green', 0.1)
    time.sleep(0.1) 
    pyautogui.press('enter') 
    pyautogui.write('We need to be sustainable', 0.1)

def todo_list():
    time.sleep(3)
    pyautogui.moveTo(500, 675)  # Move to bottom of screen
    time.sleep(0.1) 
    pyautogui.click()
    pyautogui.write("/h3", interval=0.1)
    time.sleep(0.1)                 # maybe
    pyautogui.press('enter') 
    pyautogui.write("To Do:", interval=0.1)
    pyautogui.press('enter') 
    pyautogui.write("/t", interval=0.1)
    pyautogui.press('enter') 
    pyautogui.write("Read the essay paper", interval=0.1)
    pyautogui.press('enter') 
    pyautogui.write("Ask prof. about the project", interval=0.1)
    pyautogui.press('enter') 
    pyautogui.write("Plan team meeting", interval=0.1)
    pyautogui.press('enter') 
    pyautogui.press('enter') 
    pyautogui.press('enter') 


def material():
    time.sleep(2)
    pyautogui.write("/h3", interval=0.1)
    pyautogui.press('enter') 
    pyautogui.write("Material:", interval=0.1)
    pyautogui.press('enter') 
    pyautogui.write("/f", interval=0.1)
    pyautogui.press('enter') 
    time.sleep(0.1)
    pyautogui.moveTo(877, 705)  # Move to "Choose a file"-button
    time.sleep(0.1)
    pyautogui.click()
    time.sleep(0.1)
    pyautogui.moveTo(390, 460)  # Move to "Desktop" in finder 
    time.sleep(0.5)
    pyautogui.click()
    pyautogui.moveTo(550, 350)  # Move to first element in folder
    pyautogui.click()
    pyautogui.moveTo(1025, 645)  # Move to "open"-button 
    pyautogui.click()
    time.sleep(2)
    pyautogui.scroll(-10)
    time.sleep(0.1)
    pyautogui.moveTo(450, 645) # Line under imported file i
    time.sleep(0.1)
    pyautogui.click()
    pyautogui.press('enter')
    pyautogui.write("/pa", interval=0.1)
    pyautogui.press('enter')
    pyautogui.write("Question to professor - steering meeting", interval=0.1)
    pyautogui.press('enter')
    pyautogui.write("/c", interval=0.1)
    pyautogui.press('enter')
    pyautogui.write("During the steering meeting we will have the chance to ask the professors about our project. We will get some feedback, and overview of how our progress is. The meeting is on @26.02.", interval=0.1)
    pyautogui.press('enter')
    pyautogui.write(".", interval=0.1)
    pyautogui.keyDown('shift')
    pyautogui.press('enter')
    pyautogui.write("Pia will not attend the meeting", interval=0.1)
    pyautogui.press('enter')
    pyautogui.press('enter')
    pyautogui.write("/n", interval=0.1) # notion function for numbered list
    pyautogui.press('enter')
    pyautogui.write("What is EnergyBridge?", interval=0.1)
    pyautogui.press('enter')
    pyautogui.write("When is the deadline?", interval=0.1)






# Assumes macOS
def main():
    login()
    new_page()
    create_page()
    todo_list()
    material()
    cleanup()


main()