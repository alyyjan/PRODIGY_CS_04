import time
import os

# Function to write keystrokes to a log file
def write_log(key):
    with open("keylog.txt", "a") as f:
        f.write(key)

# Main function to listen for and log keystrokes
def keylogger():
    # File to store the keystrokes
    log_file = "keylog.txt"

    # Check if the log file already exists
    if not os.path.exists(log_file):
        print("The log file doesn't exist. Creating a new log file.")
        open(log_file, 'a').close()

    # Main loop to continuously monitor keystrokes
    while True:
        # Open the log file
        with open(log_file, "a") as f:
            try:
                # Listen for a single keystroke
                key = input()
                # Write the keystroke to the log file
                write_log(key)
            except KeyboardInterrupt:
                # If Ctrl+C is pressed, exit the loop
                print("\nExiting...")
                break

if __name__ == "__main__":
    print("Keylogger started. Press Ctrl+C to stop.")

    # Start the keylogger
    keylogger()
