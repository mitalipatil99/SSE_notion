import os
import subprocess
import time
import random
import application_script
import chromewebscript
import energiBridge


def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


def warm_up():
    """Warm up by running a dummy CPU-intensive task."""
    print("Warming up with dummy task...")

    # Approach 1: Run Fibonacci sequence
    start_time = time.time()
    result = fibonacci(30)  # desired Fibonacci number
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Dummy task executed in {execution_time:.2f} seconds")

    print("Warm-up completed!")


# def run_script(script_function, count):
#     try:
#         time.sleep(3)  # Wait for 3 seconds before starting the script
#         script_function()  # Execute the script
#     except Exception as e:
#         print(f"Error running {script_function.__name__}: {e}")

quit_terminal = """
tell application "Terminal"
    quit
end tell
"""

def experiment():
    N = 30  # Number of iterations per function/test

    scripts = [
        application_script.desktop,
        chromewebscript.web
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
        time.sleep(270) 

        subprocess.run(["osascript", "-e", quit_terminal]) # quite the terminal before next iteration


if __name__ == '__main__':
    warm_up
    experiment()