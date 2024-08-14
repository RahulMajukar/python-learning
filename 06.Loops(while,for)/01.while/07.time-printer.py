import time

while True:
    # Get the current local date and time
    current_time = time.strftime("%Y-%m-%d %H:%M:%S")
    # or
    # Get the current local time
    # current_time = time.strftime("%H:%M:%S")

    # Clear the console output (platform-dependent)
    print("\033c", end="")
    # Print the current date and time
    print(f"Current date and time: {current_time}")
    # Wait for 1 second
    time.sleep(1)
