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
    notion_path = "C:\\Program Files\\Notion\\Notion.exe"
    subprocess.Popen(notion_path)
else:
    print("You're likely using Linux or macOS.")
    subprocess.run(["open", "/Applications/Notion.app"])

