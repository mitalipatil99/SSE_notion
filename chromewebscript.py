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


def new_page():
    # Create new page, no keyboard shortcut 
    time.sleep(3)
    pyautogui.moveTo(77, 258)  # Move to "new page"
    time.sleep(1)
    pyautogui.click()
    time.sleep(1)


    pyautogui.moveTo(447, 523)  # Move to "templates"-button  
    time.sleep(1)
    pyautogui.click()
    time.sleep(1)

    pyautogui.moveTo(270, 221)  # Move to "work"-dropdown  
    time.sleep(1)
    pyautogui.click()
    time.sleep(1)

    pyautogui.moveTo(298, 285)  # Move to School
    time.sleep(1)
    pyautogui.click()
    time.sleep(1)

    pyautogui.moveTo(140, 260)  # Move to search bar
    time.sleep(1)
    pyautogui.click()
    time.sleep(1)

    pyautogui.write('notes', interval=0.1)
    time.sleep(1)

    pyautogui.moveTo(180, 358)  #  Move to "Cornell"-button  
    time.sleep(1)
    pyautogui.click()
    time.sleep(1)

    pyautogui.moveTo(1222, 735)  # Change Move to get template
    pyautogui.click()
    time.sleep(1)


def create_page():
    time.sleep(3)
    # Delete the explanation
    pyautogui.scroll(-30)  # Change Move to 

    time.sleep(1)
    pyautogui.moveTo(365, 416)  # From left

    time.sleep(0.1)
    pyautogui.mouseDown()
    time.sleep(1)
    pyautogui.moveTo(1270, 153)  # To right 
    time.sleep(1)
    pyautogui.moveTo(1270, 178)  # To right 
    time.sleep(1)
    pyautogui.mouseUp()
    time.sleep(1)
    pyautogui.press('backspace')    # Delete content
    pyautogui.moveTo(900, 413)  # What does this do?? remove? 
    pyautogui.click()
    # pyautogui.moveTo(954, 365)  # Move to heading of page 
    # time.sleep(1)
    # pyautogui.click()
    # time.sleep(1)
    # Change heading
    for i in range(20):
        pyautogui.press('backspace')
    time.sleep(1)
    pyautogui.write("CS4415 - Sustainable Software Engineering", interval=0.1)
    time.sleep(2)
    pyautogui.scroll(-10)  # Scroll to bottom of page 
    time.sleep(1)
    pyautogui.moveTo(739, 367)  # Move to "Date" 
    pyautogui.click()
    time.sleep(1)
    pyautogui.press('backspace')
    time.sleep(0.1) 
    pyautogui.write("@t", interval=0.1) # write todays date by using notion shortcut @today 
    time.sleep(0.1) 
    pyautogui.press('enter') 
    pyautogui.moveTo(554, 416)  # Move to "Topic"-header 
    time.sleep(1)
    pyautogui.click()
    time.sleep(0.5)
    pyautogui.write('Green Fintech', 0.1)
    
    time.sleep(1) 
    pyautogui.moveTo(768, 544)  # Move to bullet points
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
    pyautogui.moveTo(511, 685)  # Move to bottom of screen
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
    # pyautogui.moveTo(877, 705)  # Move to "Choose a file"-button
    # time.sleep(0.1)
    # pyautogui.click()
    # time.sleep(0.1)
    # pyautogui.moveTo(390, 460)  # Move to "Desktop" in finder 
    # time.sleep(0.5)
    # pyautogui.click()
    # pyautogui.moveTo(550, 350)  # Move to first element in folder
    # pyautogui.click()
    # pyautogui.moveTo(1025, 645)  # Move to "open"-button 
    # pyautogui.click()
    # time.sleep(4)
    # pyautogui.scroll(-10)
    # time.sleep(0.1)
    # pyautogui.moveTo(450, 645) # Line under imported file i
    # time.sleep(0.1)
    # pyautogui.click()
    # pyautogui.write("/pa", interval=0.1)
    # pyautogui.press('enter')
    # pyautogui.write("Question to professor - steering meeting", interval=0.1)
    # pyautogui.press('enter')
    # pyautogui.write("/c", interval=0.1)
    # pyautogui.press('enter')
    # pyautogui.write("During the steering meeting we will have the chance to ask the professors about our project. We will get some feedback, and overview of how our progress is. The meeting is on @26.02.", interval=0.1)
    # pyautogui.press('enter')
    # pyautogui.write(".", interval=0.1)
    # pyautogui.keyDown('shift')
    # pyautogui.press('enter')
    # pyautogui.write("Pia will not attend the meeting", interval=0.1)
    # pyautogui.press('enter')
    # pyautogui.press('enter')
    # pyautogui.write("/n", interval=0.1) # notion function for numbered list
    # pyautogui.press('enter')
    # pyautogui.write("What is EnergyBridge?", interval=0.1)
    # pyautogui.press('enter')
    # pyautogui.write("When is the deadline?", interval=0.1)

def main():
    # login()
    new_page()  
    create_page()
    todo_list()
    material()


main()