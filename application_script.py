import pyautogui
import subprocess
import platform
import os


# Get the os version
# os = platform.system()
# print(f"Operating System: {os}")



# Opening application
# Dependent on OS
# 'posix' for Linux and macOS, 'nt' for Windows
if os.name == 'nt':
    print("You're using Windows.")
    notion_path = "C:\\Users\\Mitali\\Downloads\\Notion Setup 2.0.47.exe" # notion path change 
    subprocess.Popen(notion_path)
else:
    print("You're likely using Linux or macOS.")
    subprocess.run(["open", "/Applications/Notion.app"])

