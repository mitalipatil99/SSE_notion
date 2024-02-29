import time
import pyautogui
import subprocess

quit_terminal = """
tell application "Terminal"
    quit
end tell
"""

folder_path = folder_path = '/Users/piaasbjornsen/Documents/V2024/SSE/EnergyBridge/energibridge-v0.0.4-aarch64-apple-darwin'

def open_terminal():
    command = f'open -a Terminal "{folder_path}"'
    subprocess.run(command, shell=True)

def generate_command(script_function, count, total_count):
    if script_function == 'desktop':
        command = f"./energibridge -o {script_function}_{count}_{total_count}.csv --summary /Users/piaasbjornsen/Documents/V2024/SSE/SSE_notion/application_script.py"
        return command
    if script_function == 'web':
        command = f"./energibridge -o {script_function}_{count}_{total_count}.csv --summary /Users/piaasbjornsen/Documents/V2024/SSE/SSE_notion/chromewebscript.py"
        return command

# Script to be run in main
def energyBridge(command):
    open_terminal()
    time.sleep(3)
    pyautogui.write(command, interval=0.1)
    pyautogui.press('enter')
    return None
    