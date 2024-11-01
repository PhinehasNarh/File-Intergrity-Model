# I usually don't comment my code but here I am

import hashlib
import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import tkinter as tk
from tkinter import messagebox
import datetime
import yaml

#  Paths to monitor and the log file for changes
DIRECTORY_TO_MONITOR = r"C:\path\to\your\directory"  # Change this to the directory you want to keep an eye on!
LOG_FILE = r"C:\path\to\your\change_log.txt"  # Change this to where you want your change logs saved!

#  Last notification timestamp for debounce
last_notification_time = {}

# Function to generate SHA-512 hash of a file (because I want to be extra secure!)
def get_file_hash(file_path):
    sha512_hash = hashlib.sha512()  # Initiating the SHA-512 
    with open(file_path, "rb") as f:
        # Read the file in chunks to avoid memory overload
        for byte_block in iter(lambda: f.read(4096), b""):
            sha512_hash.update(byte_block)  # Update the hash with the current chunk
    return sha512_hash.hexdigest()  # Return the final hashed value

#  Logging function to record change events in YAML format (because YAML is fancy!)
def log_change(event_type, file_path):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Timestamp like a time stampede! 
    user = os.getenv("USERNAME")  # Grab the username of the heroic file warrior who made changes

    # Log event in YAML format
    log_entry = {
        "timestamp": timestamp,
        "user": user,
        "event_type": event_type,
        "file_path": file_path
    }

    #  Print debug output to console (because I like to keep it transparent!)
    print(f"Logging change: {log_entry}")  # Debug output

    with open(LOG_FILE, "a") as log_file:
        # Write our log entry in style, adding flair with YAML
        yaml.dump([log_entry], log_file, default_flow_style=False, sort_keys=False)
        log_file.write("\n")  # Separate entries with a newline for readability, like keeping your diary neat!

#  Function to show a Tkinter pop-up notification (party time!)
def show_popup(file_path, event_type):
    root = tk.Tk()
    root.withdraw()  # Hide the main Tkinter window like a magician! 
    messagebox.showinfo("File Integrity Alert", f"A {event_type} was detected on {file_path}.")
    root.destroy()  # Close the pop-up window— show’s over!

#  File event handler for detecting changes 
class FileChangeHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if not event.is_directory:  
            self.handle_event("Modified", event.src_path)

    def on_created(self, event):
        if not event.is_directory:  
            self.handle_event("Created", event.src_path)

    def on_deleted(self, event):
        if not event.is_directory:  
            self.handle_event("Deleted", event.src_path)

    def handle_event(self, event_type, file_path):
        current_time = time.time()  # Get the current time because we need to know the vibe!
        # Check if we should send a notification based on the last notification time
        if (file_path not in last_notification_time or 
            current_time - last_notification_time[file_path] > 5):  # 5 seconds debounce, keeping it cool!
            log_change(event_type, file_path)  # Log the change—like writing it in your diary!
            show_popup(file_path, event_type)  # Show the pop-up—time to celebrate!
            last_notification_time[file_path] = current_time  # Update the last notification time, keeping track of the fun!

#  Set up the observer (time to watch like a hawk!)
observer = Observer()
event_handler = FileChangeHandler()  # Create our event handler buddy
observer.schedule(event_handler, path=DIRECTORY_TO_MONITOR, recursive=True)  # Start watching our directory!

#  Starts monitoring
print("Starting file integrity monitoring... Get ready for action! 🎬")
observer.start()
try:
    while True:  # Keep the show running until we say stop!
        time.sleep(1)  # Chill out for a second before checking again
except KeyboardInterrupt:
    observer.stop()  # Stop the observer gracefully when we hit Ctrl+C
observer.join()  # Wait for the observer to finish up before we call it a day!
