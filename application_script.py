#!/usr/bin/env python
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
fullScreenC = """
tell application "System Events"
    tell application "Google Chrome" to activate
    delay 1
    keystroke "f" using {control down, command down}
end tell
"""

quit = """
tell application "Notion"
    quit
end tell
"""

quit_c = """
tell application "Google Chrome"
    quit
end tell
"""

# This function assumes 
# * Static coordinates for buttons 
def login():
    time.sleep(1)
    subprocess.run(["osascript", "-e", fullScreenC]) # Activate full screen

    time.sleep(2)
    pyautogui.moveTo(718, 546)  # Move to correct user 
    time.sleep(1)
    pyautogui.click()

    time.sleep(2)
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
    pyautogui.moveTo(1425, 22)  # Move to ... /the right corner
    pyautogui.click()   
    for i in range(12):
        pyautogui.press('down')
    pyautogui.press('enter')           

    time.sleep(1)
    subprocess.run(["osascript", "-e", fullScreen]) # exit full screen to be able to log out
    time.sleep(3)
    pyautogui.moveTo(191, 102)
    time.sleep(1)
    pyautogui.click()

    time.sleep(1)
    pyautogui.moveTo(147, 340)  # Move to log out-button
    time.sleep(1)
    pyautogui.click()

    time.sleep(2)
    subprocess.run(["osascript", "-e", quit]) # Quit the notion application
    time.sleep(1)
    subprocess.run(["osascript", "-e", quit_c]) # Open full screen

    

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

    pyautogui.moveTo(339, 118)  # Move to "work"-dropdown  
    time.sleep(1)
    pyautogui.click()
    time.sleep(1)

    pyautogui.moveTo(333, 201)  # Move to School
    time.sleep(1)
    pyautogui.click()
    time.sleep(1)

    pyautogui.moveTo(266, 171)  # Move to searchbar
    time.sleep(1)
    pyautogui.click()
    time.sleep(1)

    pyautogui.write('notes', interval=0.1)
    time.sleep(1)

    pyautogui.moveTo(233, 304)  # Move to "Cornell"-button  
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
    pyautogui.moveTo(954, 365)  # Move to heading section
    time.sleep(1)
    pyautogui.click()
    time.sleep(1)
    # Write heading
    for i in range(20):
        pyautogui.press('backspace')
    time.sleep(1)
    pyautogui.write("CS4415 - Sustainable Software Engineering", interval=0.1)
    time.sleep(2)
    pyautogui.scroll(-40)
    time.sleep(1)
    pyautogui.moveTo(764, 240)  # Move to "Date"-header 
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
    time.sleep(4)
    pyautogui.scroll(-10)
    time.sleep(0.1)
    pyautogui.moveTo(450, 645) # Line under imported file i
    time.sleep(0.1)
    pyautogui.click()
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

def go_back():
    time.sleep(2)
    pyautogui.keyDown('command')
    pyautogui.write('[')
    pyautogui.keyUp('command')
    time.sleep(1)
    pyautogui.scroll(30)
    time.sleep(1)


def math():
    time.sleep(1)
    pyautogui.moveTo(999, 830) # Move to last bullet point
    time.sleep(0.5)
    pyautogui.click()
    pyautogui.press('enter')
    pyautogui.write('Milliampere hour (mAh)', interval=0.1)
    pyautogui.press('enter')
    pyautogui.press('backspace')
    pyautogui.write('/eq', interval=0.1)
    pyautogui.press('enter')
    pyautogui.write('W=1000mAh×3.8V=3800mWh=3.8Wh=3.8×3600J=13680J', interval=0.1)
    pyautogui.press('enter')

def code():
    time.sleep(5)   # Takes aprox. 5sec to write the equation
    pyautogui.scroll(-30)
    pyautogui.moveTo(660, 417) # Move to last checkbox 
    pyautogui.click()
    time.sleep(0.1)
    pyautogui.press('enter')
    pyautogui.write('Ask Mitali to review code below', interval=0.1)
    pyautogui.press('enter')
    pyautogui.press('enter')
    pyautogui.write('/co', interval=0.1)
    pyautogui.press('enter')
    pyautogui.write('def function():', interval=0.1)
    pyautogui.press('enter')
    pyautogui.press('tab')
    pyautogui.write('i = 1', interval=0.1)
    pyautogui.press('enter')
    pyautogui.press('tab')
    pyautogui.write('for i in range(2):', interval=0.1)
    pyautogui.press('enter')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.write('i+=1', interval=0.1)
    pyautogui.moveTo(516, 503) # Move language drop-down
    pyautogui.click()
    time.sleep(0.1)
    pyautogui.write('py', interval=0.1)
    time.sleep(0.1)
    pyautogui.press('enter')

def check_todo():
    time.sleep(1)
    pyautogui.moveTo(454, 372) # Move to project todo
    pyautogui.click()


# Assumes macOS
def desktop():
    login()
    new_page()
    create_page()
    todo_list()
    material()
    go_back()
    math()
    code()
    check_todo()
    cleanup()

if __name__ == "__main__":
    desktop()