import os
import time
import random 



def fibonacci(n):
    if n<=1:
        return n
    else:
        return fibonacci(n-1)+ fibonacci(n-2)

def warm_up_dummy_task():
    """Warm up by running a dummy CPU-intensive task."""
    print("Warming up with dummy task...")

    # Approach 1: Run Fibonacci sequence
    start_time = time.time()
    result = fibonacci(30)  # Adjust the parameter for the desired Fibonacci number
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Dummy task executed in {execution_time:.2f} seconds")

    # Approach 2: Run same energy tests and discard results 1and 2  # to be decided which one to use 
    print("Warming up with energy tests (discard results in the end)...")
    # Code for running energy tests goes here

    print("Warm-up completed!")


def experiment():
    pass

