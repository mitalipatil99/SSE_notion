import os
import subprocess
import time
import random

import pyautogui
import application_script
import chromewebscript
import energiBridge

# Cleanup used in cleanup between iterations of experiment (not in experiment piepline)
# Deletes page created in prev. run
# Always used web for clean up
def cleanup():
    chromewebscript.login()
    time.sleep(4)
    pyautogui.moveTo(123, 333)  # Move to page in left sidebar
    time.sleep(1)
    pyautogui.click()   
    pyautogui.moveTo(1414, 144)  # Move to ... in right corner
    time.sleep(1)
    pyautogui.click()   
    time.sleep(2)
    pyautogui.moveTo(1300, 511)  # Move to delete
    time.sleep(1)
    pyautogui.click()

    time.sleep(2)
    chromewebscript.logout()

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)



def warm_up():
    """Warm up by running a dummy CPU-intensive task."""
    print("Warming up with dummy task...")
    start_time = time.time()
    r = 0
    i = 0
    while time.time() - start_time < 60:
        r = fibonacci(30)
        i += 1
    else:
        print(f"Warmup number: {i}th fibonacci number is {r}")
    print("Warm-up completed!")
    time.sleep(2)


quit_terminal = """
tell application "Terminal"
    quit
end tell
"""

def experiment():
    N = 30  # Number of iterations per function/test

    scripts = [
        application_script.desktop, chromewebscript.web
    ]

    # Duplicate and shuffle the list to run each script 30 times
    script_order = scripts * N
    random.shuffle(script_order)
    total_iterations = len(script_order) 

    # Dictionary to keep track of the count for each script
    script_count = {script.__name__: 0 for script in scripts}

    # Execute each script in random order
    for count, script in enumerate(script_order, start=1):
        # Increment count for the current script
        script_count[script.__name__] += 1

        # Print iteration number out of total and count for each script
        print(f"Iteration {count}/{total_iterations}, {script_count[script.__name__]}/30 for {script.__name__}")
        
        # Config
        command = energiBridge.generate_command(script.__name__, script_count[script.__name__], count)
        
        # Measures the energy consumption for the command
        result = energiBridge.energyBridge(command)

        result

        # Wait for 200 seconds before the next iteration
        time.sleep(230) 

        cleanup()
        
        subprocess.run(["osascript", "-e", quit_terminal]) # quite the terminal before next iteration
        time.sleep(60)  # Sleep for 60 sec between iterations


if __name__ == '__main__':
    warm_up()
    experiment()
